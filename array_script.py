import sys

lens_string = str(sys.argv[1:][0])

#io_path = '/pbs/home/n/nhogg/slacs/git_dolphin/results'

io_path = '/pbs/throng/lupm/hoggn/results'

from dolphin.processor import Processor

processor = Processor(io_path)

processor.swim(lens_name=lens_string, model_id='full', log=False, recipe_name='galaxy-galaxy')

