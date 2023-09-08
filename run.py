import logging
from colorama import Fore
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings, ColorPalette
from TwitchChannelPointsMiner.classes.Chat import ChatPresence
from TwitchChannelPointsMiner.classes.Settings import Priority, Events, FollowersOrder
from TwitchChannelPointsMiner.classes.entities.Bet import Strategy, BetSettings, Condition, OutcomeKeys, FilterCondition, DelayMode
from TwitchChannelPointsMiner.classes.entities.Streamer import Streamer, StreamerSettings

twitch_miner = TwitchChannelPointsMiner(
    username="PoshelNahuy",#your username on twitch
    password="", #your psw for account
    enable_analytics=True,
    claim_drops_startup=True,
    priority=[
        Priority.STREAK,
        Priority.DROPS,
        Priority.ORDER
    ],
    logger_settings=LoggerSettings(
        save=True,
        console_level=logging.INFO,
        file_level=logging.DEBUG,
        emoji=True,
        less=False, #True for short logs
        colored=True,
        color_palette=ColorPalette(
            STREAMER_online="GREEN",
            streamer_offline="red",
            BET_wiN=Fore.MAGENTA
        )
    ),
    #here that is born the magic!
    streamer_settings=StreamerSettings(
        make_predictions=False, #put true if want to make prediction
        follow_raid=True, #seguire un raid o meno +250 points easy
        claim_drops=True,
        watch_streak=True,
        chat=ChatPresence.ONLINE,               # Join irc chat to increase watch-time [ALWAYS, NEVER, ONLINE, OFFLINE]
        bet=BetSettings(
            strategy=Strategy.SMART,  # Choose you strategy!
            percentage=5,  # Place the x% of your channel points
            percentage_gap=20,  # Gap difference between outcomesA and outcomesB (for SMART strategy)
            max_points=50000,  # If the x percentage of your channel points is gt bet_max_points set this value
            stealth_mode=True,
            # If the calculated amount of channel points is GT the highest bet, place the highest value minus 1-2 points Issue #33
            delay_mode=DelayMode.FROM_END,
            # When placing a bet, we will wait until `delay` seconds before the end of the timer
            delay=6,
            minimum_points=20000,  # Place the bet only if we have at least 20k points. Issue #113
            filter_condition=FilterCondition(
                by=OutcomeKeys.TOTAL_USERS,
                # Where apply the filter. Allowed [PERCENTAGE_USERS, ODDS_PERCENTAGE, ODDS, TOP_POINTS, TOTAL_USERS, TOTAL_POINTS]
                where=Condition.LTE,  # 'by' must be [GT, LT, GTE, LTE] than value
                value=800
            )
        )
    )
)

twitch_miner.analytics(host="127.0.0.1", port=5000, refresh=10, days_ago=7)




twitch_miner.mine(
    [
        Streamer("mayhemzer0"),
        Streamer("crashdiet_05"),
        Streamer("pixelkewie"),
        Streamer("vikafromdnepr"),
        Streamer("theiathedraco"),
        Streamer("misscoookiez"),
        Streamer("florencia"),
    ],
    followers=True,
    followers_order=FollowersOrder.DESC,
    blacklist=[
        "jesusavgn",
        "alinity",
        "spb1703",
        "mira",
        "Enkk"
        "emmalayne",
        "orkpod",
        "welovechill",
        "luliziv",
        "jarl__ua"
        "annicafrost",
        "cipso_ttv"
        "bellaramatv"
        "a_couple_streams",
        "olgamelay",
        "luplupka",
        "panterochka_",
        "dayzerosec",
        "ortopilot",
        "sharishaxd",
        "candyuff",
        "ai_mori",
        "katerinasing",
        "nomadi_",
        "melina",
        "shylily",
        "vei",
    ]
)