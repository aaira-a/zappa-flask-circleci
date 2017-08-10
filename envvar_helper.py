import json


def add_aws_envvar(stage, key, value, filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        data[stage]["aws_environment_variables"][key] = value

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    import sys
    add_aws_envvar(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
