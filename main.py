import matplotlib.pyplot as plt
import get_data
import visualize

Source, ZillowMaterials = get_data.get_data()
viz = visualize.Visualize()

for key in Source:
	method_name = key # set by the command line options
	try:
		method = getattr(viz, method_name)
		plt.figure()
		method(key)
	except:
		pass
		
		
plt.show()

'''
for key in Migration:
	viz.Migration_Rates(key)		

'''