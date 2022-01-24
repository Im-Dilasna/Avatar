from telegram import ParseMode
from telegram.ext import run_async

from Avatar import dispatcher
from Avatar.modules.disable import DisableAbleCommandHandler
from Avatar.modules.helper_funcs.alternate import typing_action

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]
bubblefont = [
    "ⓐ",
    "ⓑ",
    "ⓒ",
    "ⓓ",
    "ⓔ",
    "ⓕ",
    "ⓖ",
    "ⓗ",
    "ⓘ",
    "ⓙ",
    "ⓚ",
    "ⓛ",
    "ⓜ",
    "ⓝ",
    "ⓞ",
    "ⓟ",
    "ⓠ",
    "ⓡ",
    "ⓢ",
    "ⓣ",
    "ⓤ",
    "ⓥ",
    "ⓦ",
    "ⓧ",
    "ⓨ",
    "ⓩ",
]
fbubblefont = [
    "🅐",
    "🅑",
    "🅒",
    "🅓",
    "🅔",
    "🅕",
    "🅖",
    "🅗",
    "🅘",
    "🅙",
    "🅚",
    "🅛",
    "🅜",
    "🅝",
    "🅞",
    "🅟",
    "🅠",
    "🅡",
    "🅢",
    "🅣",
    "🅤",
    "🅥",
    "🅦",
    "🅧",
    "🅨",
    "🅩",
]
squarefont = [
    "🄰",
    "🄱",
    "🄲",
    "🄳",
    "🄴",
    "🄵",
    "🄶",
    "🄷",
    "🄸",
    "🄹",
    "🄺",
    "🄻",
    "🄼",
    "🄽",
    "🄾",
    "🄿",
    "🅀",
    "🅁",
    "🅂",
    "🅃",
    "🅄",
    "🅅",
    "🅆",
    "🅇",
    "🅈",
    "🅉",
]
fsquarefont = [
    "🅰",
    "🅱",
    "🅲",
    "🅳",
    "🅴",
    "🅵",
    "🅶",
    "🅷",
    "🅸",
    "🅹",
    "🅺",
    "🅻",
    "🅼",
    "🅽",
    "🅾",
    "🅿",
    "🆀",
    "🆁",
    "🆂",
    "🆃",
    "🆄",
    "🆅",
    "🆆",
    "🆇",
    "🆈",
    "🆉",
]
bluefont = [
    "🇦 ",
    "🇧 ",
    "🇨 ",
    "🇩 ",
    "🇪 ",
    "🇫 ",
    "🇬 ",
    "🇭 ",
    "🇮 ",
    "🇯 ",
    "🇰 ",
    "🇱 ",
    "🇲 ",
    "🇳 ",
    "🇴 ",
    "🇵 ",
    "🇶 ",
    "🇷 ",
    "🇸 ",
    "🇹 ",
    "🇺 ",
    "🇻 ",
    "🇼 ",
    "🇽 ",
    "🇾 ",
    "🇿 ",
]
latinfont = [
    "𝒶",
    "𝒷",
    "𝒸",
    "𝒹",
    "ℯ",
    "𝒻",
    "ℊ",
    "𝒽",
    "𝒾",
    "𝒿",
    "𝓀",
    "𝓁",
    "𝓂",
    "𝓃",
    "ℴ",
    "𝓅",
    "𝓆",
    "𝓇",
    "𝓈",
    "𝓉",
    "𝓊",
    "𝓋",
    "𝓌",
    "𝓍",
    "𝓎",
    "𝓏",
]
linedfont = [
    "𝕒",
    "𝕓",
    "𝕔",
    "𝕕",
    "𝕖",
    "𝕗",
    "𝕘",
    "𝕙",
    "𝕚",
    "𝕛",
    "𝕜",
    "𝕝",
    "𝕞",
    "𝕟",
    "𝕠",
    "𝕡",
    "𝕢",
    "𝕣",
    "𝕤",
    "𝕥",
    "𝕦",
    "𝕧",
    "𝕨",
    "𝕩",
    "𝕪",
    "𝕫",
]


@run_async
@typing_action
def weebify(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/weebify <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def bubble(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/bubble <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bubblecharacter = bubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bubblecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def fbubble(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/fbubble <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fbubblecharacter = fbubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fbubblecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def square(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/square <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            squarecharacter = squarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, squarecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def fsquare(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/fsquare <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fsquarecharacter = fsquarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fsquarecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def blue(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/blue <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bluecharacter = bluefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bluecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def latin(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/latin <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            latincharacter = latinfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, latincharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def lined(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/lined <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            linedcharacter = linedfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, linedcharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


__mod_name__ = "StyleText"

WEEBIFY_HANDLER = DisableAbleCommandHandler("weebify", weebify)
BUBBLE_HANDLER = DisableAbleCommandHandler("bubble", bubble)
FBUBBLE_HANDLER = DisableAbleCommandHandler("fbubble", fbubble)
SQUARE_HANDLER = DisableAbleCommandHandler("square", square)
FSQUARE_HANDLER = DisableAbleCommandHandler("fsquare", fsquare)
BLUE_HANDLER = DisableAbleCommandHandler("blue", blue)
LATIN_HANDLER = DisableAbleCommandHandler("latin", latin)
LINED_HANDLER = DisableAbleCommandHandler("lined", lined)

dispatcher.add_handler(WEEBIFY_HANDLER)
dispatcher.add_handler(BUBBLE_HANDLER)
dispatcher.add_handler(FBUBBLE_HANDLER)
dispatcher.add_handler(SQUARE_HANDLER)
dispatcher.add_handler(FSQUARE_HANDLER)
dispatcher.add_handler(BLUE_HANDLER)
dispatcher.add_handler(LATIN_HANDLER)
dispatcher.add_handler(LINED_HANDLER)

__command_list__ = ["weebify"]
__command_list__ = ["bubble"]
__command_list__ = ["fbubble"]
__command_list__ = ["square"]
__command_list__ = ["fsquare"]
__command_list__ = ["blue"]
__command_list__ = ["latin"]
__command_list__ = ["lined"]
__handlers__ = [WEEBIFY_HANDLER]
__handlers__ = [BUBBLE_HANDLER]
__handlers__ = [FBUBBLE_HANDLER]
__handlers__ = [SQUARE_HANDLER]
__handlers__ = [FSQUARE_HANDLER]
__handlers__ = [BLUE_HANDLER]
__handlers__ = [LATIN_HANDLER]
__handlers__ = [LINED_HANDLER]
