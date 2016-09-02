#define all requirements in this file
min_capacity = 83

hours = 2

price = float(0.00)

instances = {   "us-east": {
			            "large": 0.12,
			            "xlarge": 0.23,
			            "2xlarge": 0.45,
			            "4xlarge": 0.774,
			            "8xlarge": 1.4,
			            "10xlarge": 2.82
			    },
			    "us-west": {
			            "large": 0.14,
			            "2xlarge": 0.413,
			            "4xlarge": 0.89,
			            "8xlarge": 1.3,
			            "10xlarge": 2.97
			    },
			}

cpu_dict = {
			'large' : 1,
			'xlarge': 2,
			'2xlarge' : 4,
			'4xlarge' : 8,
			'8xlarge' : 16,
			'10xlarge': 32
			}
