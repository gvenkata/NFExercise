
import requests, json
print "Hello World!"
raw_input("hit enter to continue")

org = "Netflix"
github_url = "https://api.github.com/orgs/" + org + "/repos"
uname = "Netflix"
gh_uname = "yogeeda"
gh_pwd = "12fivesix"

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
        print '{}'.format(repo['name'])
        count = count + 1
    
        
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
                
        print "open pull reqs:" + str(open_count)

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

        print "closed pull reqs: " + str(closed_count)



        print "total pull reqs: " + str((closed_count + open_count))
        

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
                
        print "forks:" + str(fork_count)
        print "*******************"
     
    repo_page_counter = repo_page_counter + 1
    repo_page_param = {'page': repo_page_counter}
    r = requests.get(github_url, params=repo_page_param, auth=( gh_uname, gh_pwd))
     

print "*****GRAND TOTAL REPOS****" + str(count)
