#!/usr/bin/env python3
"""Responsive Telegram listener, reusing the tested bot and question banks.

GitHub cron is a recovery trigger, not a reliable clock. The workflow runs this
listener for ten minutes and explicitly dispatches one successor. Global
concurrency keeps a single Telegram consumer. Settings still stay in Actions
secrets. Stop the loop by disabling Review bot in the Actions tab.

State is published after incoming messages and on handoff, not on every poll.
python3 bot/listen.py --seconds 600 --publish
"""
import argparse
import os
import subprocess
import time

import bot

ORIGINAL_API = bot.api
ORIGINAL_STATUS = bot.status_text


def install():
    """Keep the underlying handlers, but wait for messages instead of exiting."""
    def long_poll(method, **params):
        if method == 'getUpdates':
            params['timeout'] = 20  # below bot.api's 30-second HTTP timeout
        return ORIGINAL_API(method, **params)

    def help_text():
        return ('<b>Commands</b>\n' +
                '\n'.join('/%s: %s' % (c, d) for c, d in bot.COMMANDS) +
                '\n\nWhile the listener is running, replies normally arrive in seconds. '
                'GitHub handoffs can cause a short gap, so this is not an instant-service guarantee.'
                '\n\nTelegram Web: tap Send progress in the guide, copy the command, '
                'open Telegram Web, paste it here and press Send.'
                '\nLibrary: %s' % bot.SITE)

    def status_text(st, banks):
        return ORIGINAL_STATUS(st, banks) + '\nListener: online, command received.'

    bot.api = long_poll
    bot.help_text = help_text
    bot.status_text = status_text


def publish():
    result = subprocess.run(
        ['bash', 'tools/commit_state.sh', 'bot live state'],
        cwd=bot.ROOT, timeout=90, check=False)
    if result.returncode:
        print('State publish failed; the saved local state will be retried.')
    return result.returncode == 0


def listen(seconds=600, should_publish=False, clock=time.monotonic, pause=time.sleep):
    if not bot.TOKEN or not bot.CHAT:
        print('Telegram repository secrets are missing; refusing to start the listener.')
        return 1
    deadline = clock() + min(600, max(0, seconds))
    # Each worker picks up the latest command menu, including the updated help.
    bot.api('setMyCommands', commands=[{'command': c, 'description': d}
                                     for c, d in bot.COMMANDS])
    first = True
    total_updates = 0
    while first or clock() < deadline:
        first = False
        before = bot.load_state()
        try:
            bot.run()
            after = bot.load_state()
            after['listener'] = {
                'checked_at': bot.now().isoformat(timespec='seconds'),
                'run_id': os.environ.get('GITHUB_RUN_ID', 'local'),
                'mode': 'long-poll',
            }
            bot.save_state(after)
            changed = (after['offset'] != before['offset'] or
                       after['last_push'] != before['last_push'])
            if after['offset'] != before['offset']:
                total_updates += 1  # batches, not an exact count of messages
            if changed and should_publish:
                publish()
        except Exception as e:
            # Do not print tokens or request URLs. Persist the diagnostic only.
            detail = str(e).replace(bot.TOKEN, '[redacted]')
            st = bot.load_state()
            bot.log(st, 'listener retry: ' + detail)
            bot.save_state(st)
            print('Telegram check failed; retrying in 5 seconds.')
            pause(5)
    st = bot.load_state()
    st['listener'] = {
        'checked_at': bot.now().isoformat(timespec='seconds'),
        'run_id': os.environ.get('GITHUB_RUN_ID', 'local'),
        'mode': 'handoff',
    }
    bot.save_state(st)
    if should_publish:
        publish()
    print('Listener window complete; %d incoming batches processed.' % total_updates)
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--seconds', type=int, default=600)
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    install()
    raise SystemExit(listen(args.seconds, args.publish))
