def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
    
## List-Comprehension 
#https://www.datacamp.com/tutorial/python-list-comprehension?utm_aid=157156375191&utm_loc=9208947-&utm_mtd=-c&utm_kw=&gad_campaignid=19589720821