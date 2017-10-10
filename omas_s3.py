from __future__ import absolute_import, print_function, division, unicode_literals

__all__=['save_omas_s3',     'load_omas_s3',     'test_omas_s3']

from omas_utils import *
from omas import *

#-----------------------------
# save and load OMAS to S3
#-----------------------------
def _base_S3_uri():
    return  's3://omas3/{username}/'.format(username=os.environ['USER'])

def save_omas_s3(ods, filename, **kw):
    '''
    Save an OMAS data set to on Amazon S3 server

    :param ods: OMAS data set

    :param filename: filename to save to

    :param kw: arguments passed to the save_omas_pkl function
    '''

    save_omas_pkl(ods, filename, **kw)
    return remote_uri(_base_S3_uri(),filename,'up')

def load_omas_s3(filename):
    '''
    Load an OMAS data set from Amazon S3 server

    :param filename: filename to load from

    :return: OMAS data set
    '''

    remote_uri(_base_S3_uri()+filename, None, 'down')
    return load_omas_pkl(os.path.split(filename)[1])

def test_omas_s3(ods):
    '''
    test save and load NetCDF

    :param ods: ods

    :return: ods
    '''
    filename='test.pkl'
    save_omas_s3(ods,filename)
    ods1=load_omas_s3(filename)
    return ods1

#------------------------------
if __name__ == '__main__':
    print('='*20)

    from omas import ods_sample
    os.environ['OMAS_DEBUG_TOPIC']='s3'
    ods=ods_sample()

    ods=test_omas_s3(ods)