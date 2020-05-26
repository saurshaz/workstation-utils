import re
from os import walk, path
import shutil

keyword = 'node_modules'
start_dir = '/Users/saurabhsharma/dev/projects/slatews/'
regex = r"(.*)(?<!{a}).*({b}$)".format(a=keyword,b=keyword)

to_delete_list = []
to_ignore_list = []

def process_dir(dir_name):
	matches = re.finditer(regex, dir_name, re.MULTILINE | re.IGNORECASE)

	for matchNum, match in enumerate(matches, start=1):
	    matchGroup = match.group()
	    ends_match = matchGroup.endswith(keyword)

	    if ends_match:
	    	perfect_match = matchGroup.index(keyword)==(len(matchGroup)-len(keyword))
	    	# print "{a} , {b}, {c}".format(a=len(matchGroup),b=len(keyword), c=len(matchGroup)-len(keyword))
	    	# print matchGroup.index(keyword)
	    	# print perfect_match
	    		
	    	if perfect_match:
	    		print "{dir_name} ends with node_modules".format(dir_name = dir_name)
	    		to_delete_list.append(dir_name)
	    		shutil.rmtree(dir_name, False, None)
	    	else:
	    		to_ignore_list.append(dir_name)
	    		# print "{dir_name} does not end".format(dir_name = dir_name)



f = []
for currentpath, folders, files in walk(start_dir):
    for folder in folders:
    	if (to_ignore_list.count(folder) > 0) or (to_delete_list.count(folder) > 0):
    		break

        # print(path.join(currentpath, folder))
        process_dir(path.join(currentpath, folder))
print to_delete_list

# TODOs
# do time tracking
# add progress bar
# take inputs to start from cli
# turn into cli command
# publish to pip
# blacklist, whitelist features
# log file
# revert to soft-delete .. check .. and then upon confirm all delete all
