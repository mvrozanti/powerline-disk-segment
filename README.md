# Powerline Memory Segment
Segment for [Powerline](https://github.com/powerline/powerline) showing the current disk usage in percent or absolute values.

## Installation
    pip setup.py install

## Usage
To apply the segment, add the following to the Powerline configuration file:

    {
        "function": "powerlinedisk.disk_usage.disk_usage"
    }

For a percentage status, use the ```disk_usage_percent``` callable:

    {
        "function": "powerlinedisk.disk_usage.disk_usage_percent"
    }

The type of memory to use can be configured by passing the desired [psutil attribute name](https://pythonhosted.org/psutil/#psutil.virtual_memory) as the ``mem_type`` argument (the default is "`used`"):


    {
        "function": "powerlinedisk.disk_usage.disk_usage",
        "priority": 50,
		"args": {
		    "mem_type": "active"
		}
    }

One or two highlight groups named ```disk_usage``` and ```disk_usage_gradient``` have to be defined in the colorscheme json file. For example:

    "disk_usage":                 { "fg": "gray8", "bg": "gray0", "attr": [] },
	"disk_usage_gradient":        { "fg": "green_yellow_orange_red", "bg": "gray0", "attr": [] }

## Dependencies
The only module used is the built-in module [os](https://docs.python.org/2/library/os.html).
