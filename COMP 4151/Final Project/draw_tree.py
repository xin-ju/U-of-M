##-------------------------------------------------------------------------
# Last modified by Vinhthuy Phan, 10/01/2019
# conda install python-graphviz
# Draw a decision tree:
# dot -Tpng -o output.png output.dot -Gdpi=200
##-------------------------------------------------------------------------
from sklearn.tree import export_graphviz
import os, subprocess, sys
def save(model, X, y, output_file_name):
	feature_names = X.columns
	class_names = [ str(x) for x in y.unique() ]
	with open(output_file_name+".dot", 'w') as f:
		export_graphviz(
			model, 
			out_file=f, 
			feature_names=feature_names, 
			class_names=sorted(class_names),
			filled=True, 
			rounded=True,
		)
		command = ["dot", "-Tpng", output_file_name+".dot", "-o", output_file_name + ".png", "-Gdpi=200"]
	try:
		if sys.platform.startswith('win'):
			subprocess.check_call(command, shell=True)
		else:
			subprocess.check_call(command)
		print('Image is saved to {}.png'.format(output_file_name))
	except:
		print("Could not run dot, ie graphviz, to produce visualization")