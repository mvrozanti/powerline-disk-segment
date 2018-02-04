import os

def mem_usage(pl):
    st = os.statvfs('/')
    percentage_avail_avail = float(st.f_bavail*st.f_bsize)/(st.f_bavail*st.f_bsize + st.f_frsize*st.f_blocks)
    return [ {
        'contents': 'ƌ:{0:.2f}%'.format(percentage_avail_avail*100),
        'gradient_level': 100.0 - 100*percentage_avail_avail,
        'highlight_groups': ['disk_usage_gradient', 'disk_usage']
        } ]

