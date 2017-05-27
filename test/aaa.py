def get_all_episodes(project_id=73, fields=['code']):
    filters = [['project', 'is', {'type': 'Project', 'id': project_id}],
               ['sg_episode', 'name_is', 'BDG109']]

    ep_dict = sg.find('Shot', filters, fields)
    return ep_dict
