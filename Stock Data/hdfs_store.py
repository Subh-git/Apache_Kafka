import subprocess

def run_cmd(args_list):
    """
    Description:
        this function execute CLI commands
    """
    print('Running systrm command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text= "True")
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return, s_output

#to put csv
put_csv= run_cmd(['hdfs', 'dfs', '-put', '/home/hdoop/TestKafka/Stock.csv', '/StockData'])
print("File successfully posted in hadoop cluster: ",put_csv)


