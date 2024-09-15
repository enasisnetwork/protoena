


from enrobie.execution.service import arguments
from enrobie.execution.service import operation
from enrobie.clients import DSCClient
from enrobie.clients import DSCClientParams
from enrobie.clients import IRCClient
from enrobie.clients import IRCClientParams
from enrobie.clients import MTMClient
from enrobie.clients import MTMClientParams
from enrobie.robie import Robie
from enrobie.robie import RobieConfig



def register_dscparams(
    config: RobieConfig,
) -> None:

    params = {
        'token': 'xxXxXxXXxxXXxXXxxXx'}

    source = {
        'enable': True,
        'client': params}

    config.register(
        'dscbot',
        client=DSCClientParams,
        source=source)



def register_dscclient(
    robie: Robie,
) -> None:

    robie.register(
        'dscbot',
        client=DSCClient)



def register_ircparams(
    config: RobieConfig,
) -> None:

    params = {
        'server': 'domain.invalid',
        'nickname': 'ircbot',
        'username': 'ircbot',
        'realname': 'ircbot'}

    source = {
        'enable': True,
        'client': params}

    config.register(
        'ircbot',
        client=IRCClientParams,
        source=source)



def register_ircclient(
    robie: Robie,
) -> None:

    robie.register(
        'ircbot',
        client=IRCClient)



def register_mtmparams(
    config: RobieConfig,
) -> None:

    params = {
        'server': 'domain.invalid',
        'token': 'xxXxXxXXxxXXxXXxxXx',
        'teamid': 'xxXxXxXXxxXXxXXxxXx'}

    source = {
        'enable': True,
        'client': params}

    config.register(
        'mtmbot',
        client=MTMClientParams,
        source=source)



def register_mtmclient(
    robie: Robie,
) -> None:

    robie.register(
        'mtmbot',
        client=MTMClient)



def execution() -> None:

    config = RobieConfig(
        arguments())

    register_dscparams(config)
    register_ircparams(config)
    register_mtmparams(config)

    config.logger.start()

    robie = Robie(config)

    register_dscclient(robie)
    register_ircclient(robie)
    register_mtmclient(robie)

    operation(robie)

    config.logger.stop()



if __name__ == '__main__':
    execution()
