import sys
import hotshot.stats

stats = hotshot.stats.load(sys.argv[1])
stats.strip_dirs()
stats.sort_stats('time', 'calls')
if len(sys.argv) > 2:
    stats.print_stats(int(sys.argv[2]))
else:
    stats.print_stats(100)
