import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

exit_with_failure = False

with open(args.filename) as flake_report, open('flake8_metrics.txt',
                                               'w') as metrics_file, open(
                                                   'flake8_quality.txt',
                                                   'w') as quality_file:
    issues = []
    for l in flake_report:
        tokens = [s for s in str.split(l) if s.strip() != '']
        i = None
        try:
            count = int(tokens[0])
            exit_with_failure = True
            if tokens[1][0] == 'E':
                metrics_file.write(
                    'flake8_style_errors{{code="{}",error="{}"}} {}\n'.format(
                        tokens[1], ' '.join(tokens[2:]).replace("'", ""),
                        count))
            if tokens[1][0] == 'W':
                metrics_file.write(
                    'flake8_style_warnings{{code="{}",error="{}"}} {}\n'.
                    format(tokens[1], ' '.join(tokens[2:]).replace("'", ""),
                           count))
            if tokens[1][0] == 'N':
                metrics_file.write(
                    'flake8_naming_warnings{{code="{}",error="{}"}} {}\n'.
                    format(tokens[1], ' '.join(tokens[2:]).replace("'", ""),
                           count))
            if tokens[1][0] == 'C':
                metrics_file.write(
                    'flake8_complexity_warnings{{code="{}",error="{}"}} {}\n'.
                    format(tokens[1], ' '.join(tokens[2:]).replace("'", ""),
                           count))
            if tokens[1][0] == 'F':
                metrics_file.write(
                    'flake8_failures{{code="{}",error="{}"}} {}\n'.format(
                        tokens[1], ' '.join(tokens[2:]).replace("'", ""),
                        count))
            exit(0)
        except ValueError:
            pass
if exit_with_failure is True:
    exit(1)
