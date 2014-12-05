
import requests, json
print "Hello World!"
raw_input("hit enter to continue")

org = "Netflix"
github_url = "https://api.github.com/orgs/" + org + "/repos"
uname = "Netflix"
gh_uname = "yogeeda"
gh_pwd = "12fivesix"

rep_arr = [[],[],[],[],[]]

list_repo = []
list_open_pull = []
list_closed_pull = []
list_total_pull = []
list_fork = []

#list_repo_count = 0
#list_open_pull_count = 0
#list_closed_pull_count = 0
#list_total_pull_count = 0
#list_fork_count = 0



# List repos for an organization (in this case the org is my account)
repo_page_counter = 1
repo_page_param = {'page': repo_page_counter}
r = requests.get(github_url, params=repo_page_param, auth=( gh_uname, gh_pwd))
count = 0

while len (r.text) > 2:
    
    assert r.status_code == 200
    # For each organization repo identify the closed, open, and total pull requests
    for repo in r.json():
        rname = (repo['name'])
        #print '{}'.format(repo['name'])
        count = count + 1
        #list_repo[list_repo_count] = rname
        #list_repo_count = list_repo_count + 1
        list_repo.append(rname)
        rep_arr[0].append(rname)
        
        pull_url = "https://api.github.com/repos/" + uname + "/" + rname + "/pulls"

        open_count = 0
        open_pull_page_counter = 1
        pull_params = {'state':'open', 'page': open_pull_page_counter}
        r2 = requests.get(pull_url, params=pull_params, auth=(gh_uname, gh_pwd))

        while len (r2.text) > 2: 
            for pull in r2.json():
                #print '{}'.format(pull['id'])
                open_count = open_count + 1

            open_pull_page_counter = open_pull_page_counter + 1
            pull_params = {'state':'open', 'page': open_pull_page_counter}
            r2 = requests.get(pull_url, params=pull_params, auth=(gh_uname, gh_pwd))
                
        #print "open pull reqs:" + str(open_count)
        #list_open_pull[list_open_pull_count] = open_count
        #list_open_pull_count = list_open_pull_count + 1
        list_open_pull.append(open_count)
        rep_arr[1].append(open_count)

        
        closed_count = 0
        closed_pull_page_counter = 1
        pull_params = {'state':'closed', 'page': closed_pull_page_counter}
        r2 = requests.get(pull_url, params=pull_params, auth=(gh_uname, gh_pwd))

        while len (r2.text) > 2:     
            for pull in r2.json():
                #print '{}'.format(pull['id'])
                closed_count = closed_count + 1
                
            closed_pull_page_counter = closed_pull_page_counter + 1
            pull_params = {'state':'closed', 'page': closed_pull_page_counter}
            r2 = requests.get(pull_url, params=pull_params, auth=(gh_uname, gh_pwd))

        #print "closed pull reqs: " + str(closed_count)
        #list_closed_pull[list_closed_pull_count] = closed_count
        #list_closed_pull_count = list_closed_pull_count + 1
        list_closed_pull.append(closed_count)
        rep_arr[2].append(closed_count)


        #print "total pull reqs: " + str((closed_count + open_count))
        #list_total_pull[list_total_pull_count] = closed_count + open_count
        #list_total_pull_count = list_total_pull_count + 1
        list_total_pull.append(closed_count + open_count)
        rep_arr[3].append(closed_count + open_count)


        fork_url = "https://api.github.com/repos/" + uname + "/" + rname + "/forks"

        fork_count = 0
        fork_page_counter = 1
        fork_params = {'page': fork_page_counter}
        r2 = requests.get(fork_url, params=fork_params, auth=(gh_uname, gh_pwd))

        while len (r2.text) > 2: 
            for fork in r2.json():
                #print '{}'.format(pull['id'])
                fork_count = fork_count + 1

            fork_page_counter = fork_page_counter + 1
            fork_params = {'page': fork_page_counter}
            r2 = requests.get(fork_url, params=fork_params, auth=(gh_uname, gh_pwd))
                
        #print "forks:" + str(fork_count)
        #print "*******************"
        #list_fork[list_fork_count] = fork_count
        #list_fork_count = list_fork_count + 1
        list_fork.append(fork_count)
        rep_arr[4].append(fork_count)

     
    repo_page_counter = repo_page_counter + 1
    repo_page_param = {'page': repo_page_counter}
    r = requests.get(github_url, params=repo_page_param, auth=( gh_uname, gh_pwd))
     

print "*****GRAND TOTAL REPOS****" + str(count)

