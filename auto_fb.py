# Encoded By PyEncryptor
# A Product Of ToxicNoob
# https://github.com/Toxic-Noob

import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))