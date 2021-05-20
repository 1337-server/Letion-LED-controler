import json

from flask import Flask, render_template, request
from subprocess import call

app = Flask(__name__)

b = {
    "FLASH": "Flash White", "JUMP": "Flash", "CYCLE": "Flash 2", "FADE": "fade", "CYCLE_ALL": "cycle all",
    "KEY_F1": "Power", "KEY_F2": "Pause", "KEY_F3": "dimmer", "KEY_F4": "Bightness up",
    "KEY_F5": "White", "KEY_F8": "Red",
    "KEY_F7": "Green", "KEY_F6": "Blue", "KEY_F9": "White", "KEY_F10": "Violet",
    "KEY_F11": "Green", "KEY_F12": "Deep orange", "KEY_F13": "Light Pink",
    "KEY_F14": "Light Purple/Blue", "KEY_F15": "Light Green", "KEY_F16": "Orange",
    "KEY_F17": "Light Aqua", "KEY_F18": "Purple", "KEY_F19": "Turquoise", "KEY_F20": "Light Lime",
    "KEY_F21": "Turquoise", "KEY_F22": "Pink", "KEY_F24": "Yellow", "KEY_F23": "Aqua",
    "BTN_1": "Quicker", "BTN_2": "Slower"
}
custom_btns = {
    "DIY_1": "Custom 1", "DIY_2": "Custom 2", "DIY_3": "Custom 3",
    "DIY_4": "Custom 4", "DIY_5": "Custom 6", "DIY_6": "Custom 6"
}
# rgb_buttons used to check if the api received a valid button
rgb_buttons = ["RED_UP", "RED_DOWN", "GREEN_UP", "GREEN_DOWN", "BLUE_UP", "BLUE_DOWN",
               "DIY_1", "DIY_2", "DIY_3", "DIY_4", "DIY_5", "DIY_6"]
rgb_buttons2 = {
    "up_btns": [
        {"RED_UP": "Custom Red Up"},
        {"GREEN_UP": "Custom Green UP"},
        {"BLUE_UP": "Custom Blue Up"}
    ],
    "down_btns": [
        {"RED_DOWN": "Custom Red Down"},
        {"GREEN_DOWN": "Custom Green Down"},
        {"BLUE_DOWN": "Custom Blue Down"}
    ],
}


@app.route('/')
def hello_world():
    return render_template('main.html', buttons=b, rgb_buttons=rgb_buttons2, diy_buttons=custom_btns)


@app.route('/api', methods=['GET', 'POST'])
def api_main():
    button = request.values.get('func') if request.method == 'POST' else request.args.get('func')
    x = {'success': False}
    if button in b or button in rgb_buttons:
        call(["irsend", "send_once", " RGBLED", button])
        x['success'] = True
    return app.response_class(response=json.dumps(x, indent=4, sort_keys=True),
                              status=200,
                              mimetype='application/json')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
