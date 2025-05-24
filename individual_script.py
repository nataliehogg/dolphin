#io_path = '/pbs/home/n/nhogg/slacs/git_dolphin/results'

io_path = '/pbs/throng/lupm/hoggn/results'

from dolphin.processor import Processor

processor = Processor(io_path)

#processor.swim(lens_name='SDSSJ0728+3835', model_id='wlos_np', log=False, recipe_name='galaxy-galaxy')

processor.swim(lens_name='SDSSJ0252+0039', model_id='quicker', log=False, recipe_name='galaxy-galaxy')
