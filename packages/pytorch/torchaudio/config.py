
from jetson_containers import L4T_VERSION

if L4T_VERSION.major >= 35:    # JetPack 5.0.2 / 5.1.x
    TORCHAUDIO_VERSION = 'v2.0.1'
elif L4T_VERSION.major == 34:  # JetPack 5.0 / 5.0.1
    TORCHAUDIO_VERSION = 'v0.11.0'
elif L4T_VERSION.major == 32:  # JetPack 4
    TORCHAUDIO_VERSION = 'v0.10.0'

package['build_args'] = {
    'TORCHAUDIO_VERSION': TORCHAUDIO_VERSION,
}
