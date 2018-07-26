# WARNING!

> Most people do not need this pack. If you want to use ChatOps with StackStorm, use the st2chatops package. This is installed by default with StackStorm.
> It includes Hubot, wired up to StackStorm.
> See docs.stackstorm.com/chatops/index.html for more about how to configure ChatOps.
> Only install this pack if you are really sure you need it.

# Hubot Integration Pack

Pack that provides management/integration with Hubot

## Configuration

Copy the example configuration in [hubot.yaml.example](./hubot.yaml.example)
to `/opt/stackstorm/configs/hubot.yaml` and edit as required.

* `endpoint` - Location of Hubot HTTP endpoint (default: http://127.0.0.1:8181)

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions

* `branch`       - List the current deployed git branch of Hubot.
* `deploy`       - Deploy a specific git branch of deployed Hubot
* `restart`      - Restart Hubot
* `post_message` - Post raw text to Hubot via HTTP API
* `post_result`  - Send JSON formatted action output via hubot-stackstorm adapter
* `update_ref`   - Update the git branch of deployed Hubot

## ChatOps Aliases

* `hubot branch`            -> hubot.branch
* `hubot deploy {{branch}}` -> hubot.deploy
* `hubot restart`           -> hubot.restart
