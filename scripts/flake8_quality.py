import argparse
import hashlib
import json

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

exit_with_failure = False

with open(args.filename) as flake_report, open('flake8_quality.json',
                                               'w') as quality_file:
    issues = []
    for l in flake_report:
        # its an issue
        tokens = [s for s in str.split(l) if s.strip() != '']

        line_is_valid = False
        try:
            firsttoken = int(tokens[0])
        except ValueError:
            line_is_valid = True

        if line_is_valid is False:
            continue

        issue_location = tokens[0].split(":")
        issue_code = tokens[1]
        issue_text = ' '.join(tokens[2:]).replace("'", "")
        issue_hash = hashlib.md5(l.encode('utf-8')).hexdigest()
        issue_type = "critical"

        if tokens[1][0] == 'E':
            issue_type = "major"
        if tokens[1][0] == 'W':
            issue_type = "minor"
        if tokens[1][0] == 'N':
            issue_type = "minor"
        if tokens[1][0] == 'C':
            issue_type = "critical"
        if tokens[1][0] == 'F':
            issue_type = "major"

        exit_with_failure = True
        i = {}
        i["description"] = "[{}] {}".format(issue_code, issue_text)
        i["fingerprint"] = issue_hash
        i["severity"] = issue_type
        i["location"] = {}
        i["location"]["path"] = issue_location[0]
        i["location"]["lines"] = {"begin": issue_location[1]}
        issues.append(i)

    # dump all the issues
    json.dump(issues, quality_file, indent=2)

if exit_with_failure is True:
    exit(1)
