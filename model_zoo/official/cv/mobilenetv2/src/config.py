# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
network config setting, will be used in train.py and eval.py
"""
import os
from easydict import EasyDict as ed

def set_config(args):
    config_cpu = ed({
        "num_classes": 26,
        "image_height": 224,
        "image_width": 224,
        "batch_size": 150,
        "epoch_size": 15,
        "warmup_epochs": 0,
        "lr_max": 0.03,
        "lr_end": 0.03,
        "momentum": 0.9,
        "weight_decay": 4e-5,
        "label_smooth": 0.1,
        "loss_scale": 1024,
        "save_checkpoint": True,
        "save_checkpoint_epochs": 1,
        "keep_checkpoint_max": 20,
        "save_checkpoint_path": "./checkpoint",
        "platform": args.platform
    })
    config_gpu = ed({
        "num_classes": 1000,
        "image_height": 224,
        "image_width": 224,
        "batch_size": 150,
        "epoch_size": 200,
        "warmup_epochs": 0,
        "lr": 0.8,
        "lr_max": 0.03,
        "lr_end": 0.03,
        "momentum": 0.9,
        "weight_decay": 4e-5,
        "label_smooth": 0.1,
        "loss_scale": 1024,
        "save_checkpoint": True,
        "save_checkpoint_epochs": 1,
        "keep_checkpoint_max": 200,
        "save_checkpoint_path": "./checkpoint",
        "platform": args.platform,
        "ccl": "nccl",
    })
    config_ascend = ed({
        "num_classes": 1000,
        "image_height": 224,
        "image_width": 224,
        "batch_size": 256,
        "epoch_size": 200,
        "warmup_epochs": 4,
        "lr": 0.4,
        "lr_max": 0.03,
        "lr_end": 0.03,
        "momentum": 0.9,
        "weight_decay": 4e-5,
        "label_smooth": 0.1,
        "loss_scale": 1024,
        "save_checkpoint": True,
        "save_checkpoint_epochs": 1,
        "keep_checkpoint_max": 200,
        "save_checkpoint_path": "./checkpoint",
        "platform": args.platform,
        "ccl": "hccl",
        "device_id": int(os.getenv('DEVICE_ID', '0')),
        "rank_id": int(os.getenv('RANK_ID', '0')),
        "rank_size": int(os.getenv('RANK_SIZE', '1')),
        "run_distribute": int(os.getenv('RANK_SIZE', '1')) > 1.
    })
    config = ed({"CPU": config_cpu,
                 "GPU": config_gpu,
                 "Ascend": config_ascend})

    if args.platform not in config.keys():
        raise ValueError("Unsupport platform.")

    return config[args.platform]
