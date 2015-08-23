__author__ = 'narcis'
def date_formatter(date_string):
    d=[]
    '''
    d=date_string.split('T')
    d[0]=d[0].split('-')
    d[1]=d[1].split(':')
    d[1].pop()
    '''
    d=date_string.split('T')
    d[0]=d[0].split('-')
    d[1]=d[1].split(':')
    d[1].pop()
    return d