import logging
from awscli.customizations.commands import BasicCommand


LOG = logging.getLogger(__name__)


def hello(name):
    """Show debug info.

    Always use a pretty printed list to make it stand out more.
    """
    print("Hi {}!".format(name))


class HelloWorldError(Exception):
    """Our standard Exception."""
    pass


def awscli_initialize(cli):
    """The entry point for HelloWorld high level commands."""
    cli.register('building-command-table.main', inject_commands)


def inject_commands(command_table, session, **kwargs):
    """Basically the same as BasicCommand.add_command.

    https://github.com/aws/aws-cli/blob/master/awscli/customizations/commands.py#L282-L283
    """
    command_table['helloworld'] = HelloWorld(session)


class HelloWorld(BasicCommand):
    """Greet the user."""
    NAME = 'helloworld'
    DESCRIPTION = 'Says hello'
    SYNOPSIS = 'aws helloworld [--name Name]'
    #EXAMPLES = BasicCommand.FROM_FILE('logs', 'filter.rst', root_module=helloworld)

    ARG_TABLE = [
        {
            'name': 'name',
            'default': 'Bob',
            'help_text': 'Supply a name to say hello to (default: \'Bob\')'
        },
    ]

    UPDATE = False

    def _run_main(self, args, parsed_globals):
        """Run the command and report success."""
        logging.basicConfig(level=logging.INFO)
        for handler in logging.root.handlers:
            handler.addFilter(logging.Filter(__name__))
        self._call(args, parsed_globals)

        return 0

    def _call(self, options, parsed_globals):
        """Run the command."""
        hello(options.name)
