# aws-cli-plugins
Examples of how to add custom commands to the [aws-cli](https://github.com/aws/aws-cli).

## Setup

Install the plugin as a python package.

    pip install -U git+https://github.com/nitrocode/aws-cli-plugins.git
    aws configure set plugins.helloworld awshelloworld

## Usage

```
$ aws helloworld
Hi Bob!
$ aws helloworld --name Tom
Hi Tom!
```

## TODO

* [ ] add `say-hello` subcommand to `helloworld` used by @RichardBronosky
* [ ] add a subcommand to an existing cli
* [ ] use the correct package format e.g. used by @shiftgig

## References

* Original by [RichardBronosky](https://github.com/RichardBronosky/aws-cli-plugins) was very helpful as a base.
* Issues [aws-cli#1261](https://github.com/aws/aws-cli/issues/1261) and [aws-cli#2350](https://github.com/aws/aws-cli/issues/2350) had some insight.
* [shiftgig's awscli-console-login](https://github.com/shiftgig/awscli-console-login) registered a new command without the help message shown as expected.

