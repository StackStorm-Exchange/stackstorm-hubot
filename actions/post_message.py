import json
import requests
from six.moves.urllib.parse import urljoin

from st2common.runners.base_action import Action

__all__ = [
    'PostMessageAction'
]


class PostMessageAction(Action):
    def run(self, message, channel, user=None, whisper=False):
        endpoint = self.config['endpoint']

        if not endpoint:
            raise ValueError('Missing "endpoint" config option')

        url = urljoin(endpoint, "/hubot/st2")

        headers = {}
        headers['Content-Type'] = 'application/json'
        body = {
            'channel': channel,
            'message': message
        }

        if user:
            body['user'] = user

        if whisper:
            body['whisper'] = whisper

        data = json.dumps(body)
        response = requests.post(url=url, headers=headers, data=data)

        if response.status_code == requests.codes.ok: # pylint: disable=no-member
            self.logger.info('Message successfully posted')
        else:
            self.logger.exception('Failed to post message: %s' % (response.text))

        return True
