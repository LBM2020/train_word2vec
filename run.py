import jieba
import gensim
import argparse
import multiproessing

from process.process import strQ2B
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def read_corpus(args):
  with open(args.corpus_file,'r') as rf:
    lines = rf.readlines()
  return lines
  
def pre_process(lines):
  #对原始数据内容进行预处理，可根据数据集添加相应的处理方法
  new_lines = [strQ2B(line.replace('<content>','').replace('</content>','')) for line in lines]
  return new_lines
  
def split_words(args,lines):
  #对处理后的数据进行分词并写入文件
  word_lines = [' '.join(jieba.lcut(line)) for line in lines]#每个词之间以空格进行连接
  with open(args.inputfile,'w') as wf:
    for line in word_lines:
      wf.write(line)
      
def train(args):
  model = Word2Vec(LineSentence(args.inputfile),size = args.embedding_size,windows = 5,min_count = 5,workers = multiproessing.cpu().count())#size代表所需训练的词训练维度
  
  #保存模型文件
  model.save(args.output_model)
  
  #保存词向量文件
  model.wv.save_word2vec_format(args.output_vector,binary = False)
  
def run():
  parser = argparse.ArgumentParser()
  parser.add_argument("--corpus_file",default = None,type = str,required = True,
                      help = 'the path of raw data')
  parser.add_argument("--input_file",default = None,type = str,required = True,
                      help = 'the path of inputfile')
  parser.add_argument("--output_model",default = None,type = str,required = True,
                      help = 'the path of model')
  parser.add_argument("--output_vector",default = None,type = str,required = True,
                      help = 'the path of vector file')
  parser.add_argument("--embedding_size",default = None,type = str,required = True,
                      help = 'the dimension of vector')
  args = parser.parse_args()
  
if __name__ == '__main__':
  run()
