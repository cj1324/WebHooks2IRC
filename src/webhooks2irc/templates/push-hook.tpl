 Repo: ${repository['name']} |
 Branch: ${ref} |
 Event: ${object_kind} |
 User: ${user_name} |
 Count: ${total_commits_count} |
 % if total_commits_count != 0:
 Last Commit: ${commits[total_commits_count - 1]['message']} > ${commits[total_commits_count - 1]['url']}
 % endif
