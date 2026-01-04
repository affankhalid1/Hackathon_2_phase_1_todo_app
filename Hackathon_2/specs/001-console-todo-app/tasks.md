---
description: "Task list for Console Todo Application implementation"
---

# Tasks: Console Todo Application

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are OPTIONAL - included for this project based on testing requirements in plan.md.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths follow structure from plan.md: `src/todo_app/` with subdirectories for models, services, cli, utils

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure in src/todo_app/
- [x] T002 [P] Create __init__.py files in all directories per plan.md
- [x] T003 [P] Create main.py entry point in src/todo_app/main.py
- [x] T004 Create tests directory structure per plan.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 [P] Create Task model with dataclass in src/todo_app/models/task.py
- [x] T006 [P] Create Priority enum in src/todo_app/models/task.py
- [x] T007 [P] Implement validation functions in src/todo_app/utils/validators.py
- [x] T008 [P] Create date utility functions in src/todo_app/utils/dates.py
- [x] T009 Create TaskService class skeleton in src/todo_app/services/task_service.py
- [x] T010 Create in-memory storage structure in TaskService
- [x] T011 Create basic CLI menu structure in src/todo_app/cli/menu.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks and view all tasks in a formatted list with key details like status, priority, and due date.

**Independent Test**: Can be fully tested by adding multiple tasks with different attributes and viewing them in a list format, delivering the basic value of task management.

### Tests for User Story 1 (OPTIONAL - included per plan requirements) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T012 [P] [US1] Unit test for Task model in tests/unit/test_task.py
- [x] T013 [P] [US1] Unit test for TaskService.add_task in tests/unit/test_task_service.py
- [x] T014 [P] [US1] Unit test for TaskService.get_all_tasks in tests/unit/test_task_service.py

### Implementation for User Story 1

- [x] T015 [P] [US1] Implement Task model validation methods in src/todo_app/models/task.py
- [x] T016 [US1] Implement add_task method in src/todo_app/services/task_service.py
- [x] T017 [US1] Implement get_all_tasks method in src/todo_app/services/task_service.py
- [x] T018 [P] [US1] Create task formatter functions in src/todo_app/utils/formatters.py
- [x] T019 [US1] Implement add task CLI functionality in src/todo_app/cli/menu.py
- [x] T020 [US1] Implement view all tasks CLI functionality in src/todo_app/cli/menu.py
- [x] T021 [US1] Add input validation for task creation in src/todo_app/cli/menu.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Update and Delete Tasks (Priority: P2)

**Goal**: Enable users to modify existing tasks when requirements change or delete tasks that are no longer needed, with confirmation to prevent accidental deletion.

**Independent Test**: Can be fully tested by updating various fields of existing tasks and deleting tasks with confirmation, delivering the ability to maintain an accurate task list.

### Tests for User Story 2 (OPTIONAL - included per plan requirements) ⚠️

- [x] T022 [P] [US2] Unit test for TaskService.update_task in tests/unit/test_task_service.py
- [x] T023 [P] [US2] Unit test for TaskService.delete_task in tests/unit/test_task_service.py

### Implementation for User Story 2

- [x] T024 [US2] Implement update_task method in src/todo_app/services/task_service.py
- [x] T025 [US2] Implement delete_task method in src/todo_app/services/task_service.py
- [x] T026 [US2] Implement get_task_by_id method in src/todo_app/services/task_service.py
- [x] T027 [US2] Implement update task CLI functionality in src/todo_app/cli/menu.py
- [x] T028 [US2] Implement delete task CLI functionality with confirmation in src/todo_app/cli/menu.py
- [x] T029 [US2] Add validation for update operations in src/todo_app/cli/menu.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Search and Filter Tasks (Priority: P3)

**Goal**: Enable users to quickly find specific tasks based on keywords, status, priority, tags, or due dates to focus on what's important.

**Independent Test**: Can be fully tested by searching and filtering tasks by various criteria, delivering the ability to quickly find relevant tasks.

### Tests for User Story 3 (OPTIONAL - included per plan requirements) ⚠️

- [x] T030 [P] [US3] Unit test for TaskService.search_tasks in tests/unit/test_search_filter.py
- [x] T031 [P] [US3] Unit test for TaskService.filter_tasks in tests/unit/test_search_filter.py

### Implementation for User Story 3

- [x] T032 [US3] Implement search_tasks method in src/todo_app/services/task_service.py
- [x] T033 [US3] Implement filter_tasks method in src/todo_app/services/task_service.py
- [x] T034 [US3] Implement search CLI functionality in src/todo_app/cli/menu.py
- [x] T035 [US3] Implement filter CLI functionality in src/todo_app/cli/menu.py
- [x] T036 [US3] Add filter validation functions in src/todo_app/utils/validators.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Sort Tasks (Priority: P4)

**Goal**: Enable users to organize their tasks in different ways (by due date, priority, title, or creation date) to see them in a meaningful order.

**Independent Test**: Can be fully tested by sorting tasks in different ways, delivering the ability to organize tasks meaningfully.

### Tests for User Story 4 (OPTIONAL - included per plan requirements) ⚠️

- [x] T037 [P] [US4] Unit test for TaskService.sort_tasks in tests/unit/test_sort.py

### Implementation for User Story 4

- [x] T038 [US4] Implement sort_tasks method in src/todo_app/services/task_service.py
- [x] T039 [US4] Implement sort CLI functionality in src/todo_app/cli/menu.py
- [x] T040 [US4] Add sorting utility functions in src/todo_app/utils/sorters.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Additional Features - Mark Complete (Priority: P2/P3)

**Goal**: Enable users to toggle task completion status with timestamps as specified in functional requirements.

**Independent Test**: Can be fully tested by marking tasks as complete and incomplete, verifying timestamps are set appropriately.

### Tests for Mark Complete Feature

- [x] T041 [P] [US2] Unit test for TaskService.mark_task_complete in tests/unit/test_task_service.py

### Implementation for Mark Complete Feature

- [x] T042 [US2] Implement mark_task_complete method in src/todo_app/services/task_service.py
- [x] T043 [US2] Implement mark complete CLI functionality in src/todo_app/cli/menu.py
- [x] T044 [US2] Update Task model to handle completion timestamps in src/todo_app/models/task.py

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T045 [P] Documentation updates per quickstart.md in README.md
- [ ] T046 Error handling and validation improvements across all modules
- [ ] T047 [P] Type hint validation across all modules
- [ ] T048 [P] Additional unit tests for edge cases in tests/unit/
- [ ] T049 Performance optimization for large task lists (1000+ tasks)
- [ ] T050 Run quickstart validation and final integration testing

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for Task model in tests/unit/test_task.py"
Task: "Unit test for TaskService.add_task in tests/unit/test_task_service.py"
Task: "Unit test for TaskService.get_all_tasks in tests/unit/test_task_service.py"

# Launch all models for User Story 1 together:
Task: "Implement Task model validation methods in src/todo_app/models/task.py"
Task: "Create task formatter functions in src/todo_app/utils/formatters.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence