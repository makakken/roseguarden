import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

with open(args.filename) as flake_report, open('flake8_metrics.txt', 'w') as metrics_file:
    for l in flake_report:
        tokens = [s for s in str.split(l) if s.strip() != '']
        try:
            count = int(tokens[0])
            if tokens[1][0] == 'E':
                metrics_file.write('flake8_style_errors{{code="{}",error="{}"}} {}\n'.format(tokens[1],' '.join(tokens[2:]),count))
            if tokens[1][0] == 'W':
                metrics_file.write('flake8_style_warnings{{code="{}",error="{}"}} {}\n'.format(tokens[1],' '.join(tokens[2:]),count))
            if tokens[1][0] == 'N':
                metrics_file.write('flake8_naming_warnings{{code="{}",error="{}"}} {}\n'.format(tokens[1],' '.join(tokens[2:]),count))
            if tokens[1][0] == 'C':
                metrics_file.write('flake8_complexity_warnings{{code="{}",error="{}"}} {}\n'.format(tokens[1],' '.join(tokens[2:]),count))
            if tokens[1][0] == 'F':
                metrics_file.write('flake8_failures{{code="{}",error="{}"}} {}\n'.format(tokens[1],' '.join(tokens[2:]),count))
        except ValueError:
            pass

