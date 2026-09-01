# Lab 2 — Agile Backlog Creation & Sprint Simulation in Jira

**Dhanush S · PES1UG24AM360 · Section F**
PES University — Dept. of CSE
**Problem Statement #60 — Podcast Guest Scheduling & Outline Builder**

The Lab 1 functional and non-functional requirements were converted into Agile Epics and
User Stories in Jira, estimated with Fibonacci story points, and run across two simulated
sprints.

---

## Deliverable

| File | Contents |
|---|---|
| [Lab2_Jira_Submission.pdf](Lab2_Jira_Submission.pdf) | All six Jira screenshots + reflection answers |
| [Lab2_Jira_Submission.docx](Lab2_Jira_Submission.docx) | Editable source |

Jira project: `SE_PodcastScheduling` (key `SP`) — company-managed Scrum.

---

## Backlog

**4 Epics · 11 User Stories · 55 story points**

| Epic | Stories |
|---|---|
| 1 · Scheduling & Availability | SP-5, SP-6, SP-7, SP-8 |
| 2 · Guest Content Submission | SP-9, SP-10 |
| 3 · Episode Production Output | SP-11, SP-12, SP-13 |
| 4 · Notifications & Access Security | SP-14, SP-15 |

| Key | User Story | Priority | Pts | Sprint |
|---|---|---|---|---|
| SP-5 | Publish Availability Windows | High | 5 | 1 |
| SP-6 | Book an Interview Slot | High | 8 | 1 |
| SP-7 | Validate Slot Availability | High | 3 | 1 |
| SP-9 | Submit Talking-Point Outline | High | 5 | 1 |
| SP-14 | Booking Confirmation and Reminder | Medium | 3 | 1 |
| SP-8 | Request Reschedule | Low | 3 | 2 |
| SP-10 | Attach Biography Links | Low | 2 | 2 |
| SP-11 | Review and Approve Talking Points | Medium | 5 | 2 |
| SP-12 | Generate Run-of-Show Sheet | High | 8 | 2 |
| SP-13 | Export Production Sheet as PDF | High | 5 | 2 |
| SP-15 | Secure Episode Board Access | High | 8 | 2 |

**Sprint 1** — 5 stories, 24 points, all completed.
**Sprint 2** — 6 stories, 31 points, all completed.

Sprint 1 was the thinnest slice that still delivers value: a guest can be booked end to end
and submit talking points. Sprint 2 built the production output on top of it.

---

## Traceability — Lab 1 to Lab 2

| Lab 1 | Realised by |
|---|---|
| FR-001 | SP-6, SP-9 |
| FR-002 | SP-5 |
| FR-003 | SP-12 |
| FR-004 | SP-11 |
| FR-005 | SP-14 |
| NFR-001 | SP-13 |
| NFR-002 | SP-15 |
| UC-01 «include» Validate Slot Availability | SP-7 |
| UC-01 «extend» Request Reschedule | SP-8 |
| UC-02 «extend» Attach Biography Links | SP-10 |

Every Lab 1 requirement is represented, and no story was invented outside the scenario.
