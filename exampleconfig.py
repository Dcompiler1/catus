from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 15293388
    API_HASH = "5942c84494f1c8e1e8ac73080c8c7205"
    # the name to display in your alive message
    ALIVE_NAME = "Shukurullayev Elbek"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://torlbsbj:Bm3D6fgyiqUG7FIkww-sU84LH1I5G9xS@mel.db.elephantsql.com/torlbsbj"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1ApWapzMBu5lSl_zeucJuROcCBgQ3pOb3rZ-Lvvs2xSvTe3rskJtsX-F3v25CYZNiLwQ7-krDhjVn1LzkptYbaSo0yujSmNEZnuJJCBeqIvoUvKJSYmknWT395SELP_DglTtUk5KLi2q-jUWPfXIadgIp-aX5bGWsQ2hSfzm7NXFrpJ_AgmMl8sFZoi-GWAiEYWYk26cZxo1MYXw2t15tFZ_xzLf7jNWzqbDmOr-Sf2xw9fNSwDlcRiFQwFuET4hsy7akSdtUo9gFu88TsmhuzlwXV7jHhAoTrfB7WAkYThdmKKNIjAemSUMCzOVmyRuomHPpz80D3xzfECAZWJkIwnunnzH4rjw="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "1717885125:AAH0LVoCMCpZ348tuCP4pQZ9yxuryafBNoA"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001522836300
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
