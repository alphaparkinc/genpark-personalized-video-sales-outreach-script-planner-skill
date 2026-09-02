class PersonalizedVideoSalesOutreachScriptPlannerClient:
    def plan_personalized_video_pitch(self, prospect_profile={'name': 'Jordan Lee', 'company': 'Acme Corp', 'role': 'VP of Engineering', 'recent_milestone': 'Raised Series B'}, value_proposition='Automate backend API regression testing with AI'):
        return {
            'video_pitch_plan_id': 'vid_ptc_8812',
            'prospect_name': prospect_profile.get('name', 'Prospect'),
            'script_pacing_word_count': 115,
            'estimated_duration_seconds': 45,
            'personalized_opening_hook': 'Hey Jordan, huge congrats on Acme Corp\'s recent Series B milestone!',
            'dynamic_variable_tokens': ['{FirstName}', '{Company}', '{SeriesMilestone}'],
            'storyboard_timeline_dossier_url': 'https://video.sales.genpark.ai/pitches/8812.json'
        }
