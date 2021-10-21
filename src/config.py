# coding: utf-8

config = {

    'car': {
        'module': 'donkey_simulation',
        'constructor': 'DonkeySimulation',
        'config': {
            "host": "127.0.0.1",
            "port": 9091
        }
    },

    'communication': {
        'module': 'udp',
        'constructor': 'UdpCommunication',
        'config': {
            "host_server": "127.0.0.1",
            "port_server": 9196,
            "host_client": "127.0.0.1",
            "port_client": 9195,
        }
    },

    'policy': {
        'module': 'keras_policy',
        'constructor': 'KerasPolicy',
        'config': {
            "path": "../../models_trained/nvidia_model",
        }
    },

    'recorder': {
        'module': 'pillow_recorder',
        'constructor': 'PillowRecorder',
        'config': {
            "path": "../../data/generated_track_2",
            "format": "png"
        }
    },

}