# Bright Network Job Matcher (Ben Gregory)

Welcome to the Job Matcher!

Authored by Ben Gregory.

## Usage

To run the Job Matcher, follow these setup steps (assuming you have Python installed):

1. Clone the repo
2. Run `py -m venv venv`
3. Install requirements with `pip install -r requirements`
4. Run `py main.py` to run the script

Note that you may pass the name of a member when running the script,
or leave blank to see a report of all stored members.

## Considerations

The implementation required a few considerations to be made.

### Quality of data

The solution should be concious of the fact that the endpoints may not guarantee quality data.
If the structure of data changes, then the solution should handle gracefully.

A lightweight set of data models should be defined, to ensure trust of data.

### Efficiency

Data should be retrieved only once from the API.

### Matching logic

Some matching logic must be defined, to do a good job of providing relevant jobs.
This should involve looking at what the members have written in their requirements, and looking for matches in the job listings.

### Code readability

The code should be clear, simple to read and well documented.

## Approach

The logic behind the matcher is split across three modules - `requesters`, `models` and `main`. There's also a small `exceptions` module.

### `requesters`

The requesters module provides a wrapper around the Bright Network API endpoints, with the help of some `MatchRequester` classes. With the help of the `models` module, the list items are translated into "Model" objects.

### `models`

The `models` module is used to translate into & then store the jobs (`Job`) and members (`Member`) in
defined data structures.

The module also provides a `JobsManager` manager, which on passing in a list of `Job` objects allows
for some simple operations to be performed on the list.

These operations include two methods, both of which take a `Member` object

- `search_by_location`: finds any potential matches between each job's location and the member's bio
- `search_by_role`: finds any potential matches between each job's description and the member's bio

The searching algorithm in both cases is fairly simple - just looking for any word match in the bio. This was determined to be a reasonable approach, as the data available is fairly minimal.

### `main`

The `main` module is the entrypoint to the matching logic, and can be ran from the CLI.

It uses the requester and manager classes to get a list of "perfect" jobs for each member.
