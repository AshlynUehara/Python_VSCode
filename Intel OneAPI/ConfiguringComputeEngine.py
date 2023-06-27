import modin.config as cfg

cfg.StorageFormat.put('ray')

import modin.pandas as pd
