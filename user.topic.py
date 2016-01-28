import os,sys,numpy
from numpy import *
import sklearn
from sklearn.decomposition import PCA

user_path='/home/lizujun/datas/history.user/user.topic'
user_mat='/home/lizujun/datas/history.user/user.topic.mat'
paper_path='/home/jianyi/project/avatar/data/target/paper.topic'
paper_mat='/home/lizujun/datas/history.user/paper.topic.mat'
user_pca = '/home/lizujun/datas/history.user/user.topic.pca'
paper_pca = '/home/lizujun/datas/history.user/paper.topic.pca'
user_ids='/home/lizujun/datas/history.user/user.topic.ids'
paper_ids='/home/lizujun/datas/history.user/paper.topic.ids'

class Get_Topic_Array(object):
        def __init__(self, fn):
                self.fn = fn

        def __iter__(self):
                with open(self.fn) as in_fd:
                        arr = []
                        ids= None
                        for line in in_fd:
                                line = line.strip()
                                if len(line) == 0:
                                        continue
                                items=line.split('\t')
                                if len(items)==2:
                                        ids = str(items[0]).strip()
                                        tmp=items[1]
                                        tmps=tmp.split(' ')
                                        result=zeros(3000)
                                        for i in range(len(tmps)):
                                                topic_rate=tmps[i].split(':')
                                                if len(topic_rate)==2:
                                                        result[int(topic_rate[0])]=float(topic_rate[1])
                                        arr = result.tolist()
                                if ids is not None and result is not None:
                                        yield (ids, arr)
                                        id = None
                                        arr = []
                                        
def step_record(path_p=None,path_m=None,path_i=None,pca_c=None,mat_c=None,ids_c=None):
        st=' '
        if path_pca is not None and pca_context is not None:
                with open(path_pca,'w') as pca_pca:
                        for i in range(len(pca_context)):
                                print >> pca_pca, st.join(str(e) for e in (pca_context[i].tolist()))
        if path_mat is not None and mat_context is not None:
                with open(path_mat,'w') as mat:
                        string_topic = st.join(str(e) for e in (values).tolist())
                        print >> mat, string_topic
        if path_ids is not None and ids_context is not None:
                with open(path_ids,'w') as item_ids:
                        string_ids = st.join(ids)
                        print >> item_ids, string_ids
def Run_Pca(fn,path_pca=None,path_mat=None,path_ids=None,record=False):
        ids = []
        values = None
        gt = Get_Topic_Array(fn)
        for t in gt:
                context = [t[0],t[1]]
                ids.append(context[0])
                a = numpy.array([context[1]])
                if values is not None:
                        values = numpy.concatenate((values, a), axis=0)
                        #np_array_out=vstack((np_array_out,a))
                        pass
                else:
                        values=a
                        pass

        pca=PCA(n_components=100)
        newdata=pca.fit_transform(values)
        if record:
                step_record(path_p=path_pca,path_m=path_mat,path_i=path_ids,pca_c=newdata,mat_c=values,ids_c=ids)
                
if __name__ == "__main__":
        #Run_Pca(user_path,path_pca=user_pca,path_mat=user_mat,path_ids=user_ids,record=True)
        Run_Pca(paper_path,path_pca=paper_pca,path_mat=paper_mat,path_ids=paper_ids,record=True)
