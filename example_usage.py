from client import PersonalizedVideoSalesOutreachScriptPlannerClient

def main():
    client = PersonalizedVideoSalesOutreachScriptPlannerClient()
    res = client.plan_personalized_video_pitch({'name': 'Elena Rostova', 'company': 'FinTech Labs'})
    print('Personalized Video Pitch Planner: ' + res['video_pitch_plan_id'] + ' (Duration: ' + str(res['estimated_duration_seconds']) + 's)')
    print('Opening Hook: "' + res['personalized_opening_hook'] + '"')
    print('Variable Tokens: ' + ', '.join(res['dynamic_variable_tokens']))
    print('Storyboard URL: ' + res['storyboard_timeline_dossier_url'])

if __name__ == '__main__':
    main()
