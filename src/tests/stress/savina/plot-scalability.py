import sys
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')
cores = [2, 4, 8, 16, 32, 64]

def plot(ax, encore, akka, name):
  ax.plot(cores, encore, 'bo-', label="Encore")
  ax.plot(cores, akka, 'r^-', label="Akka")
  ax.set_title(name)
  ax.set_xlabel('#cores', fontsize=16)
  ax.set_ylabel('time (sec)', fontsize=16)

def finalisePlot(bm):
  plt.legend(loc='best', shadow=True, fontsize=16)
  plt.savefig(bm + '_scalability.pdf', format='pdf', pad_inches=0, bbox_inches='tight') 

def getSecFromMinutes(t):
  """ 0:04.67"""
  aux=t.split(":")
  minutes=int(aux[0])
  sms=float(aux[1])
  r= float(minutes*60) + sms
  return r

def getSecFromMS(t):
  """3882.501"""
  return float(t)/1000

def read_file(fn):
  with open(fn) as f:
    return f.readlines()

def newRun(di, cores, tt):
  t = di.get(cores, list())
  t.append(tt)    
  di[cores] = t 

def final_numbers(results):
  times=[]
  for cc in cores:
    xs = results.get(cc)
    # Remove two worse times from the 12 executions
    xs.remove(max(xs))
    xs.remove(max(xs))
    times.append(np.average(xs))
  return times

def parse_encore(fn): 
  """Cores: 2 :: Input:  :: Iteration: 4 :: Time: 0:09.03"""
  results={} # cores --> list of times
  for line in read_file(fn):
    words=line.split(" :: ")
    cc=int(words[0].split(" ")[1])
    iteration=int(words[2].split(" ")[1])
    tt=getSecFromMinutes(words[3].split(" ")[1])
    newRun(results, cc, tt)
  return final_numbers(results)

def parse_akka(fn):
  curr_core = 0
  results={} # cores --> list of times
  for line in read_file(fn): 
    if "Core count:" in line: 
      curr_core = int(line.split(":")[1])
    elif "Iteration-" in line: 
      ms = getSecFromMS(line.split(":")[1].replace(" ms", ""))
      newRun(results, curr_core, ms)
  return final_numbers(results)

def parseAndPlot(ax, encore_path, akka_path, bm):
  encore=parse_encore(encore_path)
  akka=parse_akka(akka_path)
  plot(ax, encore, akka, bm)

f, ax = plt.subplots(1, 1)
enc_loc = sys.argv[1]
akka_loc= sys.argv[2]
benchmark = sys.argv[3]

parseAndPlot(ax, enc_loc, akka_loc, benchmark)
finalisePlot(benchmark)
