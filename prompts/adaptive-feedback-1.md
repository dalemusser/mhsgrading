# Task: Generate Teacher-Facing Feedback for Yellow Progress Points

## Project Context

This repository contains documentation and code used to design and develop a teacher dashboard for the serious game **Mission HydroSci**.

In the dashboard:

* Each **column** represents one progress point in the game.
* Each **row** represents one player, identified by an in-game player ID.
* Each **cell** represents the player’s performance on a specific progress point.
* A cell is colored **green** or **yellow** according to the grading logic for that progress point.
* When a teacher hovers over a yellow cell, a pop-up text box should explain:

  1. how the player performed;
  2. why the progress point was classified as yellow;
  3. which available in-game resources or strategies the player may not have used effectively;
  4. which knowledge or skill may require additional support;
  5. what interventions an instructor could provide.

The feedback is intended for teachers and instructors, not for students.

## Available Information

Use the following files and folders as evidence.

### 1. Game Storyline and Task Context

The folder:

`feedback-message-for-each-pp/game-combo-doc`

contains live combination documents describing the storyline, dialogue, task sequence, and detailed game content for each unit.

Use these documents to understand what the player was expected to do and what information was presented during gameplay.

### 2. Curriculum Goals

The folder:

`feedback-message-for-each-pp/curriculum-goal-for-each-pp`

contains the curriculum goals for each progress point.

Currently, curriculum-goal documentation is available only for progress points in **Units 1 and 2**.

Use these documents to identify the specific knowledge and skills targeted by each progress point.

### 3. Available Resources and Strategies

The folder:

`feedback-message-for-each-pp/potential-strategy-for-each-pp`

describes the information, scaffolds, tools, feedback, and strategies available to players during each progress point.

Currently, this documentation is available only for progress points in **Units 1 and 2**.

Use these documents to determine which resources could have helped the player complete the task. Do not state that the player failed to use a resource unless the gameplay logs provide evidence supporting that conclusion. When usage cannot be confirmed, use cautious wording such as:

* “The player may not have used...”
* “The available logs do not show evidence that the player used...”
* “The player may have benefited from...”

### 4. Assessment Rubrics

The folder:

`feedback-message-for-each-pp/assessment-score-rubric-for-each-pp`

contains the scoring rubric for each progress point.

Use the rubric to explain what performance was expected and why the observed performance did not meet the green-performance threshold.

### 5. Grading Logic

The folder:

`grading-logic`

contains the programming logic used to assign a green or yellow color to each progress point.

The progress point represented by each file can be inferred from its filename. For example:

`mhs-unit1-point3-grading.md`

contains the grading logic for Unit 1, Progress Point 3.

Treat the grading logic as the authoritative source for determining why a cell is yellow.

### 6. Test Gameplay Logs and Expected Results

The gameplay logs from a previous test playthrough are stored in:

`playthrough-logs-and-results/05-01-26`

The expected dashboard colors are documented in:

`playthrough-logs-and-results/05-01-26/TEST_RESULTS.md`

The expected colors, in dashboard order, are:

`Green, Green, Yellow, Green, Green, Yellow, Green, Green, Green, Green, Yellow`

Use the progress-point order defined by the dashboard, grading files, or test documentation to map these colors to their corresponding progress points. Do not assume the mapping solely from the position in the list if an explicit mapping is available elsewhere.

## Goal

Generate the teacher-facing pop-up feedback for every progress point in **Units 1 and 2** that is expected to appear yellow for the test player represented in `playthrough-logs-and-results/05-01-26`.

The feedback should help a teacher quickly understand:

* what the player did;
* which grading condition produced the yellow result;
* what the observed behavior may indicate;
* which in-game supports may have helped;
* what instructional intervention may be appropriate.

## Required Analysis Procedure

For each yellow progress point:

1. Identify the corresponding unit and progress-point number.
2. Read the relevant grading-logic file.
3. Read the assessment rubric.
4. Read the curriculum-goal description.
5. Read the available-resource and strategy description.
6. Review the relevant game-content documentation.
7. Locate the player events in the test logs that are used by the grading logic.
8. Reconstruct the player’s observable performance.
9. Explain exactly which grading condition caused the yellow result.
10. Distinguish direct log evidence from interpretation.
11. Generate concise and actionable teacher-facing feedback.

## Evidence and Inference Requirements

### Directly Supported Statements

Use definitive wording only for facts directly supported by the logs or grading code.

Examples:

* “The player submitted an incorrect argument on the first attempt.”
* “The player needed five attempts to complete the matching task.”
* “The logs do not contain the event required for a green result.”
* “The player selected waterfall height instead of flow rate.”

### Interpretive Statements

Use cautious wording when describing possible knowledge weaknesses or strategy-use problems.

Examples:

* “This may indicate difficulty distinguishing relevant evidence from other collected observations.”
* “The player may need additional support connecting flow rate with relative watershed size.”
* “The player may not have fully used the comparison table or the available review dialogue.”
* “The current logs cannot determine whether the player misunderstood the concept or made an accidental selection.”

### Prohibited Inferences

Do not claim that the player:

* definitely misunderstood a concept;
* ignored a resource;
* did not read a dialogue;
* was disengaged;
* guessed;
* was confused;
* intentionally avoided a tool;

unless the logs provide direct evidence for that conclusion.

Do not infer emotions, motivation, attention, or intent from an incorrect answer alone.

## Feedback Content Requirements

Each pop-up description should contain the following sections.

### Performance Summary

Briefly state what the player did and why the progress point received a yellow result.

### Evidence from Gameplay

Identify the relevant logged action, attempt count, selected answer, completion time, missing event, or other observable evidence used by the grading logic.

### Possible Learning Need

Explain what curriculum knowledge or skill may require additional support. Clearly label this as an interpretation rather than a confirmed diagnosis.

### Potentially Underused Support

Identify relevant in-game resources or strategies that may have helped the player. Use cautious wording unless resource usage can be directly verified from the logs.

### Suggested Instructor Intervention

Recommend one or more specific actions the instructor could take. The intervention should directly address the identified task and curriculum goal.

Possible interventions include:

* reviewing a key concept;
* asking the student to explain their reasoning;
* revisiting an instructional video;
* comparing correct and incorrect examples;
* guiding the student through a map or evidence table;
* providing a similar practice problem;
* prompting the student to distinguish relevant from irrelevant evidence.

## Writing Requirements

The generated feedback should be within a new markdown file. The feedback should be:

* written for teachers or instructors;
* concise enough to fit in a dashboard pop-up;
* specific to the player and progress point;
* understandable without reading the source code;
* evidence-based;
* nonjudgmental;
* actionable;
* free of unsupported diagnostic claims.

Avoid vague descriptions such as:

* “The player did poorly.”
* “The student does not understand the concept.”
* “More practice is needed.”

Instead, identify the specific observed behavior and the precise concept or strategy involved.

## Required Output Format

Create one Markdown section for each yellow progress point.

Use the following structure:

```markdown
## Unit [Number], Progress Point [Number]: [Progress-Point Name]

**Yellow-result trigger:**  
[Exact grading condition that produced the yellow result.]

**Performance summary:**  
[Concise explanation of the player’s observable performance.]

**Gameplay evidence:**  
- [Relevant log event, answer, attempt count, duration, or missing record.]
- [Additional supporting evidence, when available.]

**Possible learning need:**  
[Cautious interpretation of the curriculum knowledge or skill that may require support.]

**Potentially underused support:**  
[Relevant in-game resource, scaffold, dialogue, tool, or strategy that may have helped. State uncertainty when usage cannot be verified.]

**Suggested instructor intervention:**  
[Specific and actionable instructional response.]

**Dashboard pop-up text:**  
[A polished, concise paragraph suitable for direct display in the teacher dashboard.]
```

## Dashboard Pop-Up Style

The final `Dashboard pop-up text` should normally contain approximately **80–150 words**.

It should follow this general sequence:

1. observed performance;
2. reason for the yellow classification;
3. possible learning or strategy need;
4. recommended teacher support.

Example style:

> The player completed the topographic-map matching task, but required five attempts, which resulted in a yellow classification. The repeated mismatches may indicate difficulty connecting contour-line patterns in the top-down map with the corresponding side-view terrain profile. The player may have benefited from reviewing DANI’s contour-line guidance or comparing elevation and slope patterns before submitting each match. Consider asking the student to explain how closely and widely spaced contour lines represent terrain shape, and then provide a short map-to-profile matching exercise.

Do not copy this example unless it accurately matches the player’s actual evidence.

## Final Verification

Before completing the task:

1. Confirm that every generated section corresponds to a progress point expected to be yellow.
2. Confirm that each yellow explanation matches the grading code.
3. Confirm that all stated gameplay behavior appears in the test logs.
4. Confirm that curriculum interpretations align with the documented curriculum goal.
5. Confirm that suggested resources exist in the strategy documentation or game content.
6. Confirm that unsupported interpretations are expressed cautiously.
7. Report any missing, inconsistent, or contradictory documentation rather than silently resolving it.

If the expected color conflicts with the grading code or gameplay logs, please follow the expected colors, instead of the actual colors summarized from the gameplay log in units 1 and 2.