import json
import example10


print(json.dumps(example10.spec.to_dict(), indent=2))