"""GitLab v4 API description."""
DEFAULT_URL = 'https://gitlab.com'
API_PATH = '/api/v4'

MAPPING = {
    'project_id': {
        'events': {
            'method': ['GET'],
            'path': '/${project_id}/events',
        },
    },
    'application': {
        'settings': {
            'path': '/application/settings',
            'method': ['GET', 'PUT'],
        },
    },
    'applications': {
        'path': '/applications',
        'method': ['POST'],
    },
    'broadcast_messages': {
        'method': ['GET', 'POST'],
        'path': '/broadcast_messages',
        'id': {
            'method': ['DELETE', 'GET', 'PUT'],
            'path': '/broadcast_messages/${id}',
        },
    },
    'circuit_breakers': {
        'repository_storage': {
            'method': ['DELETE', 'GET'],
            'path': '/circuit_breakers/repository_storage',
        },
        'repository_storage/failing': {
            'method': ['GET'],
            'path': '/circuit_breakers/repository_storage/failing',
        },
    },
    'deploy_keys': {
        'method': ['GET'],
        'path': '/deploy_keys',
    },
    'events': {
        'method': ['GET'],
        'path': '/events',
    },
    'features': {
        'method': ['GET'],
        'path': '/features',
        'name': {
            'method': ['POST'],
            'path': '/features/${name}',
        },
    },
    'groups': {
        'method': ['GET', 'POST'],
        'path': '/groups',
        'id': {
            'method': ['DELETE', 'GET', 'PUT'],
            'path': '/groups/${id}',
            'access_requests': {
                'method': ['GET', 'POST'],
                'path': '/groups/${id}/access_requests',
                'user_id': {
                    'method': ['DELETE'],
                    'path': '/groups/${id}/access_requests/${user_id}',
                    'approve': {
                        'method': ['PUT'],
                        'path': '/groups/${id}/access_requests/${user_id}/approve',
                    },
                },
            },
            'custom_attributes': {
                'path': '/groups/${id}/custom_attributes',
                'key': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/groups/${id}/custom_attributes/${key}',
                },
            },
            'issues': {
                'method': ['GET'],
                'path': '/groups/${id}/issues',
            },
            'members': {
                'method': ['GET', 'POST'],
                'path': '/groups/${id}/members',
                'user_id': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/groups/${id}/members/${user_id}',
                },
            },
            'milestones': {
                'method': ['GET', 'POST'],
                'path': '/groups/${id}/milestones',
                'milestone_id': {
                    'method': ['GET', 'PUT'],
                    'path': '/groups/${id}/milestones/${milestone_id}',
                    'issues': {
                        'method': ['GET'],
                        'path': '/groups/${id}/milestones/${milestone_id}/issues',
                    },
                    'merge_requests': {
                        'method': ['GET'],
                        'path': '/groups/${id}/milestones/${milestone_id}/merge_requests',
                    },
                },
            },
            'notification_settings': {
                'method': ['GET', 'PUT'],
                'path': '/groups/${id}/notification_settings',
            },
            'projects': {
                'method': ['GET'],
                'path': '/groups/${id}/projects',
            },
            'subgroups': {
                'method': ['GET'],
                'path': '/groups/${id}/subgroups',
            },
            'variables': {
                'method': ['GET', 'POST'],
                'path': '/groups/${id}/variables',
                'key': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/groups/${id}/variables/${key}',
                },
            },
        },
    },
    'hooks': {
        'method': ['GET', 'POST'],
        'path': '/hooks',
        'id': {
            'method': ['DELETE', 'GET'],
            'path': '/hooks/${id}',
        },
    },
    'issues': {
        'method': ['GET'],
        'path': '/issues',
    },
    'keys': {
        'id': {
            'method': ['GET'],
            'path': '/keys/${id}',
        },
    },
    'lint': {
        'method': ['POST'],
        'path': '/lint',
    },
    'merge_requests': {
        'method': ['GET'],
        'path': '/merge_requests',
    },
    'namespaces': {
        'method': ['GET'],
        'path': '/namespaces',
        'id': {
            'path': '/namespaces/${id}',
        },
    },
    'notification_settings': {
        'method': ['GET', 'PUT'],
        'path': '/notification_settings',
    },
    'pages': {
        'domains': {
            'method': ['GET'],
            'path': '/pages/domains',
        },
    },
    'projects': {
        'method': ['GET', 'POST'],
        'path': '/projects',
        'id': {
            'method': ['DELETE', 'GET', 'PUT'],
            'path': '/projects/${id}',
            'access_requests': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/access_requests',
                'user_id': {
                    'method': ['DELETE'],
                    'path': '/projects/${id}/access_requests/${user_id}',
                    'approve': {
                        'method': ['PUT'],
                        'path': '/projects/${id}/access_requests/${user_id}/approve',
                    },
                },
            },
            'archive': {
                'method': ['POST'],
                'path': '/projects/${id}/archive',
            },
            'boards': {
                'method': ['GET'],
                'path': '/projects/${id}/boards',
                'board_id': {
                    'method': ['GET'],
                    'path': '/projects/${id}/boards/${board_id}',
                    'lists': {
                        'method': ['GET', 'POST'],
                        'path': '/projects/${id}/boards/${board_id}/lists',
                        'list_id': {
                            'method': ['DELETE', 'GET', 'PUT'],
                            'path': '/projects/${id}/boards/${board_id}/lists/${list_id}',
                        },
                    },
                },
            },
            'custom_attributes': {
                'method': ['GET'],
                'path': '/projects/${id}/custom_attributes',
                'key': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/custom_attributes/${key}',
                },
            },
            'deploy_keys': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/deploy_keys',
                'key_id': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/deploy_keys/${key_id}',
                },
            },
            'deployments': {
                'method': ['GET'],
                'path': '/projects/${id}/deployments',
                'deployment_id': {
                    'method': ['GET'],
                    'path': '/projects/${id}/deployments/${deployment_id}',
                },
            },
            'environments': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/environments',
                'environment_id': {
                    'method': ['DELETE', 'PUT'],
                    'path': '/projects/${id}/environments/${environment_id}',
                    'stop': {
                        'method': ['POST'],
                        'path': '/projects/${id}/environments/${environment_id}/stop',
                    },
                },
            },
            'fork': {
                'method': ['DELETE', 'POST'],
                'path': '/projects/${id}/fork',
                'forked_from_id': {
                    'method': ['POST'],
                    'path': '/projects/${id}/fork/${forked_from_id}',
                },
            },
            'forks': {
                'method': ['GET'],
                'path': '/projects/${id}/forks',
            },
            'hooks': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/hooks',
                'hook_id': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/hooks/${hook_id}',
                },
            },
            'housekeeping': {
                'method': ['POST'],
                'path': '/projects/${id}/housekeeping',
            },
            'issues': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/issues',
                'issue_iid': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/issues/${issue_iid}',
                    'add_spent_time': {
                        'method': ['POST'],
                        'path': '/projects/${id}/issues/${issue_iid}/add_spent_time',
                    },
                    'award_emoji': {
                        'method': ['GET', 'POST'],
                        'path': '/projects/${id}/issues/${issue_iid}/award_emoji',
                        'award_id': {
                            'method': ['DELETE', 'GET'],
                            'path': '/projects/${id}/issues/${issue_iid}/award_emoji/${award_id}',
                        },
                    },
                    'closed_by': {
                        'method': ['GET'],
                        'path': '/projects/${id}/issues/${issue_iid}/closed_by',
                    },
                    'move': {
                        'method': ['POST'],
                        'path': '/projects/${id}/issues/${issue_iid}/move',
                    },
                    'notes': {
                        'method': ['GET', 'POST'],
                        'path': '/projects/${id}/issues/${issue_iid}/notes',
                        'note_id': {
                            'method': ['DELETE', 'GET', 'PUT'],
                            'path': '/projects/${id}/issues/${issue_iid}/notes/${note_id}',
                            'award_emoji': {
                                'method': ['GET', 'POST'],
                                'path': '/projects/${id}/issues/${issue_iid}/notes/${note_id}/award_emoji',
                                'award_id': {
                                    'method': ['DELETE', 'GET'],
                                    'path': '/projects/${id}/issues/${issue_iid}/notes/${note_id}/award_emoji/${award_id}',
                                },
                            },
                        },
                    },
                    'participants': {
                        'method': ['GET'],
                        'path': '/projects/${id}/issues/${issue_iid}/participants',
                    },
                    'reset_spent_time': {
                        'method': ['POST'],
                        'path': '/projects/${id}/issues/${issue_iid}/reset_spent_time',
                    },
                    'reset_time_estimate': {
                        'method': ['POST'],
                        'path': '/projects/${id}/issues/${issue_iid}/reset_time_estimate',
                    },
                    'subscribe': {
                        'method': ['POST'],
                        'path': '/projects/${id}/issues/${issue_iid}/subscribe',
                    },
                    'time_estimate': {
                        'method': ['POST'],
                        'path': '/projects/${id}/issues/${issue_iid}/time_estimate',
                    },
                    'time_stats': {
                        'method': ['GET'],
                        'path': '/projects/${id}/issues/${issue_iid}/time_stats',
                    },
                    'todo': {
                        'method': ['POST'],
                        'path': '/projects/${id}/issues/${issue_iid}/todo',
                    },
                    'unsubscribe': {
                        'method': ['POST'],
                        'path': '/projects/${id}/issues/${issue_iid}/unsubscribe',
                    },
                    'user_agent_detail': {
                        'method': ['GET'],
                        'path': '/projects/${id}/issues/${issue_iid}/user_agent_detail',
                    },
                },
            },
            'jobs': {
                'method': ['GET'],
                'path': '/projects/${id}/jobs',
                'artifacts': {
                    'ref_name': {
                        'download': {
                            'method': ['GET'],
                            'path': '/projects/:id/jobs/artifacts/${ref_name}/download',
                        }
                    }
                },
                'job_id': {
                    'method': ['GET'],
                    'path': '/projects/${id}/jobs/${job_id}',
                    'artifacts': {
                        'method': ['GET'],
                        'path': '/projects/${id}/jobs/${job_id}/artifacts',
                        'artifact_path': {
                            'method': ['GET'],
                            'path': '/projects/${id}/jobs/${job_id}/artifacts/${artifact_path}',
                        },
                        'keep': {
                            'method': ['POST'],
                            'path': '/projects/${id}/jobs/${job_id}/artifacts/keep',
                        },
                    },
                    'cancel': {
                        'method': ['POST'],
                        'path': '/projects/${id}/jobs/${job_id}/cancel',
                    },
                    'erase': {
                        'method': ['POST'],
                        'path': '/projects/${id}/jobs/${job_id}/erase',
                    },
                    'play': {
                        'method': ['POST'],
                        'path': '/projects/${id}/jobs/${job_id}/play',
                    },
                    'retry': {
                        'method': ['POST'],
                        'path': '/projects/${id}/jobs/${job_id}/retry',
                    },
                    'trace': {
                        'method': ['GET'],
                        'path': '/projects/${id}/jobs/${job_id}/trace',
                    },
                },
            },
            'labels': {
                'method': ['DELETE', 'GET', 'POST', 'PUT'],
                'path': '/projects/${id}/labels',
                'label_id': {
                    'subscribe': {
                        'method': ['POST'],
                        'path': '/projects/${id}/labels/${label_id}/subscribe',
                    },
                    'unsubscribe': {
                        'method': ['POST'],
                        'path': '/projects/${id}/labels/${label_id}/unsubscribe',
                    },
                },
            },
            'members': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/members',
                'user_id': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/members/${user_id}',
                },
            },
            'merge_requests': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/merge_requests',
                'merge_request_iid': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/merge_requests/${merge_request_iid}',
                    'add_spent_time': {
                        'method': ['POST'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/add_spent_time',
                    },
                    'award_emoji': {
                        'method': ['GET', 'POST'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/award_emoji',
                        'award_id': {
                            'method': ['DELETE', 'GET'],
                            'path': '/projects/${id}/merge_requests/${merge_request_iid}/award_emoji/${award_id}',
                        },
                    },
                    'cancel_merge_when_pipeline_succeeds': {
                        'method': ['PUT'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/cancel_merge_when_pipeline_succeeds',
                    },
                    'changes': {
                        'method': ['GET'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/changes',
                    },
                    'closes_issues': {
                        'method': ['GET'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/closes_issues',
                    },
                    'commits': {
                        'method': ['GET'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/commits',
                    },
                    'merge': {
                        'method': ['PUT'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/merge',
                    },
                    'notes': {
                        'method': ['GET', 'POST'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/notes',
                        'note_id': {
                            'method': ['DELETE', 'GET', 'PUT'],
                            'path': '/projects/${id}/merge_requests/${merge_request_iid}/notes/${note_id}',
                        },
                    },
                    'participants': {
                        'method': ['GET'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/participants',
                    },
                    'pipelines': {
                        'method': ['GET'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/pipelines',
                    },
                    'reset_spent_time': {
                        'method': ['POST'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/reset_spent_time',
                    },
                    'reset_time_estimate': {
                        'method': ['POST'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/reset_time_estimate',
                    },
                    'subscribe': {
                        'method': ['POST'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/subscribe',
                    },
                    'time_estimate': {
                        'method': ['POST'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/time_estimate',
                    },
                    'time_stats': {
                        'method': ['GET'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/time_stats',
                    },
                    'todo': {
                        'method': ['POST'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/todo',
                    },
                    'unsubscribe': {
                        'method': ['POST'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/unsubscribe',
                    },
                    'versions': {
                        'method': ['GET'],
                        'path': '/projects/${id}/merge_requests/${merge_request_iid}/versions',
                        'version_id': {
                            'method': ['GET'],
                            'path': '/projects/${id}/merge_requests/${merge_request_iid}/versions/${version_id}',
                        },
                    },
                },
            },
            'milestones': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/milestones',
                'milestone_id': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/milestones/${milestone_id}',
                    'issues': {
                        'method': ['GET'],
                        'path': '/projects/${id}/milestones/${milestone_id}/issues',
                    },
                    'merge_requests': {
                        'method': ['GET'],
                        'path': '/projects/${id}/milestones/${milestone_id}/merge_requests',
                    },
                },
            },
            'notification_settings': {
                'method': ['GET', 'PUT'],
                'path': '/projects/${id}/notification_settings',
            },
            'pages': {
                'domains': {
                    'method': ['GET', 'POST'],
                    'path': '/projects/${id}/pages/domains',
                    'domain': {
                        'method': ['DELETE', 'GET', 'PUT'],
                        'path': '/projects/${id}/pages/domains/${domain}',
                    },
                },
            },
            'pipeline': {
                'method': ['POST'],
                'path': '/projects/${id}/pipeline',
            },
            'pipeline_schedules': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/pipeline_schedules',
                'pipeline_schedule_id': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/pipeline_schedules/${pipeline_schedule_id}',
                    'take_ownership': {
                        'method': ['POST'],
                        'path': '/projects/${id}/pipeline_schedules/${pipeline_schedule_id}/take_ownership',
                    },
                    'variables': {
                        'method': ['POST'],
                        'path': '/projects/${id}/pipeline_schedules/${pipeline_schedule_id}/variables',
                        'key': {
                            'method': ['DELETE', 'PUT'],
                            'path': '/projects/${id}/pipeline_schedules/${pipeline_schedule_id}/variables/${key}',
                        },
                    },
                },
            },
            'pipelines': {
                'method': ['GET'],
                'path': '/projects/${id}/pipelines',
                'pipeline_id': {
                    'method': ['GET'],
                    'path': '/projects/${id}/pipelines/${pipeline_id}',
                    'cancel': {
                        'method': ['POST'],
                        'path': '/projects/${id}/pipelines/${pipeline_id}/cancel',
                    },
                    'jobs': {
                        'method': ['GET'],
                        'path': '/projects/${id}/pipelines/${pipeline_id}/jobs',
                    },
                    'retry': {
                        'method': ['POST'],
                        'path': '/projects/${id}/pipelines/${pipeline_id}/retry',
                    },
                },
            },
            'protected_branches': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/protected_branches',
                'name': {
                    'method': ['DELETE', 'GET'],
                    'path': '/projects/${id}/protected_branches/${name}',
                },
            },
            'repository': {
                'archive': {
                    'method': ['GET'],
                    'path': '/projects/${id}/repository/archive',
                },
                'blobs': {
                    'sha': {
                        'method': ['GET'],
                        'path': '/projects/${id}/repository/blobs/${sha}',
                        'raw': {
                            'method': ['GET'],
                            'path': '/projects/${id}/repository/blobs/${sha}/raw',
                        },
                    },
                },
                'branches': {
                    'method': ['GET', 'POST'],
                    'path': '/projects/${id}/repository/branches',
                    'branch': {
                        'method': ['DELETE', 'GET'],
                        'path': '/projects/${id}/repository/branches/${branch}',
                        'protect': {
                            'method': ['PUT'],
                            'path': '/projects/${id}/repository/branches/${branch}/protect',
                        },
                        'unprotect': {
                            'method': ['PUT'],
                            'path': '/projects/${id}/repository/branches/${branch}/unprotect',
                        },
                    },
                },
                'commits': {
                    'method': ['GET', 'POST'],
                    'path': '/projects/${id}/repository/commits',
                    'sha': {
                        'method': ['GET'],
                        'path': '/projects/${id}/repository/commits/${sha}',
                        'cherry_pick': {
                            'method': ['POST'],
                            'path': '/projects/${id}/repository/commits/${sha}/cherry_pick',
                        },
                        'comments': {
                            'method': ['GET', 'POST'],
                            'path': '/projects/${id}/repository/commits/${sha}/comments',
                        },
                        'diff': {
                            'method': ['GET'],
                            'path': '/projects/${id}/repository/commits/${sha}/diff',
                        },
                        'statuses': {
                            'method': ['GET'],
                            'path': '/projects/${id}/repository/commits/${sha}/statuses',
                        },
                    },
                },
                'compare': {
                    'method': ['GET'],
                    'path': '/projects/${id}/repository/compare',
                },
                'contributors': {
                    'method': ['GET'],
                    'path': '/projects/${id}/repository/contributors',
                },
                'files': {
                    'file_path': {
                        'method': ['DELETE', 'GET', 'POST', 'PUT'],
                        'path': '/projects/${id}/repository/files/${file_path}',
                        'raw': {
                            'method': ['GET'],
                            'path': '/projects/${id}/repository/files/${file_path}/raw',
                        },
                    },
                },
                'merged_branches': {
                    'method': ['DELETE'],
                    'path': '/projects/${id}/repository/merged_branches',
                },
                'tags': {
                    'method': ['GET', 'POST'],
                    'path': '/projects/${id}/repository/tags',
                    'tag_name': {
                        'method': ['DELETE', 'GET'],
                        'path': '/projects/${id}/repository/tags/${tag_name}',
                        'release': {
                            'method': ['POST', 'PUT'],
                            'path': '/projects/${id}/repository/tags/${tag_name}/release',
                        },
                    },
                },
                'tree': {
                    'method': ['GET'],
                    'path': '/projects/${id}/repository/tree',
                },
            },
            'runners': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/runners',
                'runner_id': {
                    'method': ['DELETE'],
                    'path': '/projects/${id}/runners/${runner_id}',
                },
            },
            'services': {
                'asana': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/asana',
                },
                'assembla': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/assembla',
                },
                'bamboo': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/bamboo',
                },
                'bugzilla': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/bugzilla',
                },
                'buildkite': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/buildkite',
                },
                'campfire': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/campfire',
                },
                'custom-issue-tracker': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/custom-issue-tracker',
                },
                'drone-ci': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/drone-ci',
                },
                'emails-on-push': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/emails-on-push',
                },
                'external-wiki': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/external-wiki',
                },
                'flowdock': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/flowdock',
                },
                'gemnasium': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/gemnasium',
                },
                'hipchat': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/hipchat',
                },
                'irker': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/irker',
                },
                'jira': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/jira',
                },
                'kubernetes': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/kubernetes',
                },
                'mattermost': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/mattermost',
                },
                'mattermost-slash-commands': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/mattermost-slash-commands',
                },
                'microsoft_teams': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/microsoft_teams',
                },
                'mock-ci': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/mock-ci',
                },
                'packagist': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/packagist',
                },
                'pipelines-email': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/pipelines-email',
                },
                'pivotaltracker': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/pivotaltracker',
                },
                'prometheus': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/prometheus',
                },
                'pushover': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/pushover',
                },
                'redmine': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/redmine',
                },
                'slack': {
                    'method': ['DELETE', 'GET', 'PUT'],
                'path': '/projects/${id}/services/slack',
                },
                'slack-slash-commands': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/slack-slash-commands',
                },
                'teamcity': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/services/teamcity',
                },
            },
            'share': {
                'method': ['POST'],
                'path': '/projects/${id}/share',
                'group_id': {
                    'method': ['DELETE'],
                    'path': '/projects/${id}/share/${group_id}',
                },
            },
            'snippets': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/snippets',
                'snippet_id': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/snippets/${snippet_id}',
                    'award_emoji': {
                        'method': ['GET', 'POST'],
                        'path': '/projects/${id}/snippets/${snippet_id}/award_emoji',
                        'award_id': {
                            'method': ['DELETE', 'GET'],
                            'path': '/projects/${id}/snippets/${snippet_id}/award_emoji/${award_id}',
                        },
                    },
                    'notes': {
                        'method': ['GET', 'POST'],
                        'path': '/projects/${id}/snippets/${snippet_id}/notes',
                        'note_id': {
                            'method': ['DELETE', 'GET', 'PUT'],
                            'path': '/projects/${id}/snippets/${snippet_id}/notes/${note_id}',
                        },
                    },
                    'raw': {
                        'method': ['GET'],
                        'path': '/projects/${id}/snippets/${snippet_id}/raw',
                    },
                    'user_agent_detail': {
                        'method': ['GET'],
                        'path': '/projects/${id}/snippets/${snippet_id}/user_agent_detail',
                    },
                },
            },
            'star': {
                'method': ['POST'],
                'path': '/projects/${id}/star',
            },
            'statuses': {
                'sha': {
                    'method': ['POST'],
                    'path': '/projects/${id}/statuses/${sha}',
                },
            },
            'triggers': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/triggers',
                'trigger_id': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/triggers/${trigger_id}',
                    'take_ownership': {
                        'method': ['POST'],
                        'path': '/projects/${id}/triggers/${trigger_id}/take_ownership',
                    },
                },
            },
            'unarchive': {
                'method': ['POST'],
                'path': '/projects/${id}/unarchive',
            },
            'unstar': {
                'method': ['POST'],
                'path': '/projects/${id}/unstar',
            },
            'uploads': {
                'method': ['POST'],
                'path': '/projects/${id}/uploads',
            },
            'users': {
                'method': ['GET'],
                'path': '/projects/${id}/users',
            },
            'variables': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/variables',
                'key': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/variables/${key}',
                },
            },
            'wikis': {
                'method': ['GET', 'POST'],
                'path': '/projects/${id}/wikis',
                'slug': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/projects/${id}/wikis/${slug}',
                },
            },
            'projects/user/${user_id}': {
                'method': ['POST'],
                'path': '/projects/user/${user_id}',
            },
        },
    },
    'runners': {
        'method': ['GET'],
        'path': '/runners',
        'id': {
            'method': ['DELETE', 'GET', 'PUT'],
            'path': '/runners/${id}',
            'jobs': {
                'path': '/runners/${id}/jobs',
            },
        },
        'all': {
            'method': ['GET'],
            'path': '/runners/all',
        },
    },
    'sidekiq': {
        'compound_metrics': {
            'method': ['GET'],
            'path': '/sidekiq/compound_metrics',
        },
        'job_stats': {
            'method': ['GET'],
            'path': '/sidekiq/job_stats',
        },
        'process_metrics': {
            'method': ['GET'],
            'path': '/sidekiq/process_metrics',
        },
        'queue_metrics': {
            'method': ['GET'],
            'path': '/sidekiq/queue_metrics',
        },
    },
    'snippets': {
        'method': ['GET', 'POST'],
        'path': '/snippets',
        'id': {
            'method': ['DELETE', 'GET', 'PUT'],
            'path': '/snippets/${id}',
            'user_agent_detail': {
                'path': '/snippets/${id}/user_agent_detail',
            },
        },
        'public': {
            'method': ['GET'],
            'path': '/snippets/public',
        },
    },
    'templates': {
        'gitignores': {
            'method': ['GET'],
            'path': '/templates/gitignores',
            'key': {
                'path': '/templates/gitignores/${key}',
            },
        },
        'gitlab_ci_ymls': {
            'method': ['GET'],
            'path': '/templates/gitlab_ci_ymls',
            'key': {
                'path': '/templates/gitlab_ci_ymls/${key}',
            },
        },
        'licenses': {
            'method': ['GET'],
            'path': '/templates/licenses',
            'key': {
                'path': '/templates/licenses/${key}',
            },
        },
    },
    'todos': {
        'method': ['GET'],
        'path': '/todos',
        'id': {
            'mark_as_done': {
                'method': ['POST'],
                'path': '/todos/${id}/mark_as_done',
            },
        },
        'mark_as_done': {
            'method': ['POST'],
            'path': '/todos/mark_as_done',
        },
    },
    'user': {
        'method': ['GET'],
        'path': '/user',
        'activities': {
            'path': '/user/activities',
        },
        'emails': {
            'method': ['GET', 'POST'],
            'path': '/user/emails',
            'email_id': {
                'method': ['DELETE', 'GET'],
                'path': '/user/emails/${email_id}',
            },
        },
        'gpg_keys': {
            'method': ['GET', 'POST'],
            'path': '/user/gpg_keys',
            'key_id': {
                'method': ['DELETE', 'GET'],
                'path': '/user/gpg_keys/${key_id}',
            },
        },
        'keys': {
            'method': ['GET', 'POST'],
            'path': '/user/keys',
            'key_id': {
                'method': ['DELETE', 'GET'],
                'path': '/user/keys/${key_id}',
            },
        },
    },
    'users': {
        'method': ['GET', 'POST'],
        'path': '/users',
        'id': {
            'method': ['DELETE', 'GET', 'PUT'],
            'path': '/users/${id}',
            'block': {
                'method': ['POST'],
                'path': '/users/${id}/block',
            },
            'custom_attributes': {
                'path': '/users/${id}/custom_attributes',
                'key': {
                    'method': ['DELETE', 'GET', 'PUT'],
                    'path': '/users/${id}/custom_attributes/${key}',
                },
            },
            'emails': {
                'method': ['GET', 'POST'],
                'path': '/users/${id}/emails',
                'email_id': {
                    'method': ['DELETE'],
                    'path': '/users/${id}/emails/${email_id}',
                },
            },
            'events': {
                'method': ['GET'],
                'path': '/users/${id}/events',
            },
            'gpg_keys': {
                'method': ['GET', 'POST'],
                'path': '/users/${id}/gpg_keys',
                'key_id': {
                    'method': ['DELETE', 'GET'],
                    'path': '/users/${id}/gpg_keys/${key_id}',
                },
            },
            'keys': {
                'method': ['GET', 'POST'],
                'path': '/users/${id}/keys',
                'key_id': {
                    'method': ['DELETE'],
                    'path': '/users/${id}/keys/${key_id}',
                },
            },
            'unblock': {
                'method': ['POST'],
                'path': '/users/${id}/unblock',
            },
        },
        'user_id': {
            'impersonation_tokens': {
                'method': ['GET', 'POST'],
                'path': '/users/${user_id}/impersonation_token',
                'impersonation_token_id': {
                    'method': ['DELETE', 'GET'],
                    'path': '/users/${user_id}/impersonation_tokens/${impersonation_token_id}',
                },
            },
            'projects': {
                'method': ['GET'],
                'path': '/users/${user_id}/projects',
            },
        },
    },
    'version': {
        'method': ['GET'],
        'path': '/version',
    },
}



def auth(self):
    """Set authentication."""
    self.headers.update({'Private-Token': self.token})
    return self.headers
