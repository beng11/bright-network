import models
import requesters
import exceptions
import random


def do_matching(selected_member: str | None = None) -> bool:
    """Do matching for either a given member, or for all available members.
    
    Returns `True` if `selected_member` is passed and has data against them.
    """

    members = requesters.MembersRequester().to_models()
    jobs = requesters.JobsRequester().to_models()

    for member in members:
        if selected_member and selected_member != member.name.lower():
            continue

        if not selected_member:
            print(f"\n------ {member.name} ------")

        manager = models.JobsManager(jobs)

        perfect_matches = manager.search_by_location(member).search_by_role(member).to_str()

        if perfect_matches:
            print("Perfect matches:", ", ".join(perfect_matches))
        else:
            suitable_by_location = manager.search_by_location(member).to_str()
            suitable_by_role = manager.search_by_role(member).to_str()
        
            if not (suitable_by_location or suitable_by_role):
                print(f"No good fit for {member.name}!")
                print(f"How about {random.choice(jobs)}?")
            else:
                print(f"Good for location:", ", ".join(suitable_by_location))
                print(f"Good for role:", ", ".join(suitable_by_role))
        
        if selected_member:
            return True
    return False


if __name__ == "__main__":    
    selected_member = input("Member name (leave empty for all): ")

    if selected_member:
        print(f"Finding {selected_member}'s dream job...")
        selected_member = selected_member.lower()

    try:
        match_result = do_matching(selected_member)
    except exceptions.MatchException as e:
        print(f"There was an error getting the data: {str(e)}")
        exit()

    if selected_member and match_result:
        exit()

    if selected_member:
        print(f"We have no data for {selected_member}!")
