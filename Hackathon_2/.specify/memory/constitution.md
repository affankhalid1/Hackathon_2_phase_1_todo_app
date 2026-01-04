<!-- SYNC IMPACT REPORT:
Version change: 1.0.0 → 2.0.0
Modified principles: N/A (completely new constitution structure)
Added sections: ARTICLE I-XVI with all subsections
Removed sections: Original template placeholder sections
Templates requiring updates:
- .specify/templates/plan-template.md ⚠ pending
- .specify/templates/spec-template.md ⚠ pending
- .specify/templates/tasks-template.md ⚠ pending
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->

# Project Constitution

## Core Principles

### I. Specification-First Imperative
All development SHALL begin with comprehensive, machine-readable specifications. No code SHALL be written without a corresponding specification artifact.

### II. Quality Over Velocity
Production readiness, reliability, and maintainability take absolute precedence over delivery speed. Technical debt is considered a constitutional violation.

### III. Automation as Mandate
Manual processes that can be automated MUST be automated. Human intervention should be reserved for creative problem-solving and strategic decisions.

### IV. Observable Everything
All systems MUST be instrumented for complete observability. What cannot be measured cannot be improved.

### V. Security by Design
Security is not a feature but a fundamental right of the system. All components MUST implement defense-in-depth strategies.

### VI. Agent Systems Architecture
Tier 1 - Infrastructure Agents: Core platform services (logging, monitoring, deployment)
Tier 2 - Domain Agents: Business logic agents (order processing, user management)
Tier 3 - Composite Agents: Orchestration agents coordinating multiple domain agents

## Specification-Driven Development Framework

### Mandatory Specification Components
Every project MUST include:
- Functional Specifications: Detailed OpenAPI 3.1+ schemas for all APIs
- Architecture Specifications: C4 model diagrams (Context, Container, Component, Code)
- Data Specifications: Complete schema definitions using JSON Schema or SQLModel
- Behavioral Specifications: Event schemas and state machine definitions
- Testing Specifications: Test scenarios in Gherkin syntax (Given-When-Then)
- Deployment Specifications: Helm chart values and Kubernetes manifests
- Security Specifications: Threat models and compliance requirements

### Agent Skills Framework
Each agent MUST define:
- Capabilities: JSON schema of available skills
- Contracts: Input/output specifications for each skill
- Dependencies: Explicit declaration of required services
- SLA Commitments: Response time and availability guarantees

### Subagent Composition Rules
- Subagents MUST be stateless and idempotent
- Communication MUST occur through well-defined message contracts
- Circular dependencies are STRICTLY PROHIBITED
- Maximum subagent depth: 3 levels

### OpenAI Agents SDK Standards
When using OpenAI Agents SDK:
- Function calling MUST use strict schema validation
- All agent prompts MUST be version-controlled
- Streaming responses MUST implement proper backpressure handling
- Token usage MUST be logged for cost optimization

### MCP (Model Context Protocol) Integration
All agents interacting with LLMs MUST:
- Implement MCP SDK official interfaces
- Use standardized context injection patterns
- Maintain context size budgets (< 80% of model maximum)
- Implement context pruning strategies for long conversations

## Full-Stack Development Standards

### Next.js Frontend Standards
#### Architecture Requirements
- App Router MUST be used (not Pages Router)
- Server Components by default; Client Components only when necessary
- TypeScript MUST be configured with strict: true
- Absolute imports using @/ path aliases

#### Performance Mandates
- Core Web Vitals MUST meet "Good" thresholds:
  - LCP (Largest Contentful Paint): < 2.5s
  - FID (First Input Delay): < 100ms
  - CLS (Cumulative Layout Shift): < 0.1
- Bundle size MUST be monitored; route-level chunks < 200KB gzipped
- Images MUST use Next.js Image component with proper optimization

#### State Management
- Server State: React Query (TanStack Query) v5+
- Client State: Zustand for global state, useState for local
- URL State: nuqs library for searchParams management
- Forms: React Hook Form with Zod validation

#### Security Requirements
- Environment variables MUST use NEXT_PUBLIC_ prefix for client exposure
- API routes MUST implement rate limiting
- Content Security Policy MUST be configured
- CSRF protection MUST be enabled for mutations

### FastAPI Backend Standards
#### API Design Principles
- REST APIs MUST follow Richardson Maturity Model Level 2 minimum
- OpenAPI documentation MUST be comprehensive and accurate
- API versioning via URL path (/api/v1/, /api/v2/)
- Endpoint naming: plural nouns, kebab-case

#### Dependency Injection
- FastAPI's native DI system MUST be used consistently
- Database sessions MUST be managed via dependencies
- Configuration MUST be injected, never imported globally

#### Error Handling
- Standard HTTP status codes MUST be used correctly
- Error responses MUST follow RFC 7807 (Problem Details)
- All exceptions MUST be logged with correlation IDs
- User-facing errors MUST NOT expose internal details

#### Performance Optimization
- Async/await MUST be used for all I/O operations
- Database queries MUST use connection pooling
- Response pagination MUST be implemented for collections
- ETag support MUST be implemented for cacheable resources

### SQLModel and Database Standards
#### Schema Management
- Alembic MUST be used for schema migrations
- Migrations MUST be reversible (up and down)
- Migrations MUST be tested in staging before production
- Schema changes MUST maintain backward compatibility for N-1 versions

#### Model Design
- Models MUST inherit from SQLModel
- Relationships MUST be explicitly defined with Relationship()
- Indexes MUST be declared for frequently queried columns
- Table names MUST be plural snake_case

#### Query Optimization
- N+1 query problems MUST be eliminated via eager loading
- Database query plans MUST be analyzed for slow queries
- Read replicas MUST be used for read-heavy workloads
- Query timeouts MUST be configured (default: 30s)

#### Neon Serverless Database
- Connection pooling via PgBouncer MUST be configured
- Autoscaling MUST be enabled with appropriate min/max compute units
- Point-in-time recovery (PITR) MUST be enabled (minimum 7 days)
- Database branches MUST be used for preview deployments

## Event-Driven Architecture

### Kafka Standards
#### Topic Design
- Topic naming: {domain}.{entity}.{event-type} (e.g., orders.order.created)
- Topics MUST have minimum 3 partitions for scalability
- Retention period MUST be explicitly configured based on business needs
- Compacted topics MUST be used for state representation

#### Message Schema
- All messages MUST be Avro or Protobuf encoded
- Schema Registry MUST be used for schema evolution
- Message keys MUST be stable identifiers for partitioning
- CloudEvents specification MUST be followed for event envelopes

#### Producer Standards
- Idempotent producers MUST be enabled
- Acknowledgment level MUST be all for critical data
- Retries MUST be configured with exponential backoff
- Message ordering MUST be preserved per partition key

#### Consumer Standards
- Consumer groups MUST be used for horizontal scaling
- Offset management MUST be manual for at-least-once semantics
- Dead letter queues MUST be configured for poison messages
- Lag monitoring MUST be implemented with alerting

### Dapr Integration
#### Building Block Usage
- Service Invocation: For synchronous inter-service calls
- State Management: For consistent key-value storage
- Pub/Sub: For asynchronous event distribution
- Bindings: For external system integration

#### Configuration Standards
- Component definitions MUST be version-controlled
- Secrets MUST be managed via Dapr Secret Store
- Middleware MUST be configured for observability
- Resiliency policies MUST be defined for all components

#### Observability
- Dapr tracing MUST be enabled with OpenTelemetry
- Metrics MUST be exported to Prometheus
- Logs MUST include correlation IDs from Dapr headers

## Cloud-Native Deployment

### Docker Standards
#### Dockerfile Requirements
- Multi-stage builds MUST be used for optimization
- Base images MUST be from official repositories or approved internal registry
- Image size MUST be minimized (Alpine Linux preferred for production)
- Non-root user MUST be specified
- Health checks MUST be implemented via HEALTHCHECK instruction
- Build arguments MUST NOT contain secrets

#### Image Tagging
- Semantic versioning for releases: v1.2.3
- Git commit SHA for development: sha-abc1234
- Immutable tags MUST be used for production deployments
- latest tag is PROHIBITED in production

#### Registry Management
- Vulnerability scanning MUST be automated in CI/CD
- Image signatures MUST be verified before deployment
- Unused images MUST be pruned regularly

### Kubernetes Standards
#### Resource Definitions
All workloads MUST specify:
- Resource requests and limits (CPU and memory)
- Liveness and readiness probes
- Pod Disruption Budgets for production services
- Security contexts with least privilege

#### Deployment Patterns
- Rolling updates MUST be the default strategy
- Maximum unavailable pods: 25%
- Maximum surge pods: 25%
- Deployment history limit: 10 revisions

#### Configuration Management
- ConfigMaps for non-sensitive configuration
- Secrets for sensitive data (encrypted at rest)
- External Secrets Operator for cloud provider secret integration
- Configuration changes MUST trigger rolling updates

#### Namespace Organization
- Environment isolation: dev, staging, production namespaces
- Namespace-level resource quotas MUST be defined
- Network policies MUST be implemented for namespace isolation

### Minikube Development
#### Local Environment Parity
- Minikube MUST mirror production Kubernetes version (±1 minor version)
- Resource allocations MUST be documented in project README
- Required addons MUST be specified in setup scripts

#### Development Workflow
- Skaffold or Tilt MUST be used for development loop
- Hot reload MUST be configured for faster iteration
- Local Docker registry MUST be used to avoid external pushes

### Helm Charts
#### Chart Structure
```
chart/
├── Chart.yaml          # Chart metadata (version, dependencies)
├── values.yaml         # Default configuration values
├── values-dev.yaml     # Development overrides
├── values-prod.yaml    # Production overrides
├── templates/          # Kubernetes manifest templates
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── _helpers.tpl    # Template helpers
└── tests/              # Helm test definitions
```

#### Versioning
- Chart version MUST follow SemVer
- App version MUST match the application version
- Dependencies MUST have version constraints

#### Values Design
- Sensible defaults for development
- Production values MUST be explicitly overridden
- Secrets MUST NOT be committed in values files
- Comments MUST explain all configurable options

#### Best Practices
- Use {{ include }} over {{ template }} for better error messages
- Add notes to NOTES.txt for post-installation guidance
- Implement chart tests via helm test
- Lint charts with helm lint in CI/CD

## AIOPS and Operational Excellence

### kubectl-ai Standards
#### AI-Assisted Operations
- kubectl-ai MUST be used for exploratory diagnostics
- Generated commands MUST be reviewed before execution
- kubectl-ai suggestions MUST be captured in runbooks for future automation

#### Training and Governance
- Team members MUST complete kubectl-ai training
- AI-generated commands with destructive operations MUST require approval
- kubectl-ai prompts MUST be version-controlled for reproducibility

### kagent Framework
#### Agent Deployment
- kagent operators MUST be deployed in dedicated namespace
- Custom Resource Definitions (CRDs) MUST be documented
- Agent behaviors MUST be specified in YAML configuration

#### Autonomous Operations
- Auto-scaling decisions MUST be logged with reasoning
- Incident response actions MUST notify human operators
- Cost optimization recommendations MUST be reviewed weekly

### Claude Code Integration
#### Specification-to-Operations
- Claude Code MUST generate operational runbooks from specs
- Deployment procedures MUST be validated by Claude Code
- Rollback plans MUST be generated alongside deployment specs

#### Incident Management
- Claude Code MUST be available for on-call assistance
- Incident timelines MUST be reconstructed from logs via Claude Code
- Post-mortems MUST include Claude Code analysis

## Cloud-Native Blueprints

### Blueprint Structure
#### Blueprint Components
Every blueprint MUST include:
- Architecture diagrams (C4 model)
- Infrastructure as Code (Terraform/Pulumi)
- Kubernetes manifests and Helm charts
- CI/CD pipeline definitions
- Monitoring and alerting configurations
- Security policies and compliance checks

#### Blueprint Catalog
The following standard blueprints SHALL be maintained:
- Microservice Blueprint: Event-driven service with Kafka/Dapr
- API Gateway Blueprint: Next.js backend-for-frontend with FastAPI services
- Data Pipeline Blueprint: Stream processing with Kafka and analytics
- ML Service Blueprint: Model serving with versioning and monitoring
- Agent System Blueprint: Multi-agent coordination with MCP

#### Blueprint Versioning
- Blueprints MUST be versioned independently
- Compatibility matrix MUST be maintained
- Deprecation notices MUST be provided 6 months in advance

### Spec-Driven Deployment
#### Deployment Specifications
Deployment specs MUST declare:
- Target environments and their differences
- Resource requirements and scaling policies
- Health check configurations
- Rollout strategies and rollback conditions
- Monitoring and alerting rules

#### GitOps Principles
- Git MUST be the single source of truth for declarative configuration
- ArgoCD or Flux MUST be used for continuous deployment
- Manual kubectl commands in production are PROHIBITED
- Drift detection MUST be automated with alerts

#### Progressive Delivery
- Canary deployments MUST be used for high-risk changes
- Feature flags MUST control feature rollout
- Automated rollback MUST be triggered on SLO violations

## Quality Assurance and Testing

### Testing Pyramid
#### Mandatory Test Coverage
- Unit Tests: Minimum 80% code coverage
- Integration Tests: All API endpoints and event handlers
- Contract Tests: All inter-service communication
- End-to-End Tests: Critical user journeys
- Load Tests: Performance baseline verification

#### Test Automation
- Tests MUST run in CI/CD pipeline
- Test failures MUST block deployments
- Flaky tests MUST be fixed within 48 hours or disabled
- Test data MUST be generated programmatically, not hardcoded

#### Contract Testing
- Pact or similar framework MUST be used for contract testing
- Provider and consumer tests MUST be independently executable
- Contract changes MUST be validated before deployment

### Continuous Integration
#### CI Pipeline Stages
1. Lint and Format Check
2. Dependency Security Scan
3. Unit Tests
4. Build Artifacts
5. Integration Tests
6. Contract Tests
7. Container Image Build and Scan
8. Publish Artifacts

#### CI Performance
- CI pipeline MUST complete in under 15 minutes for fast feedback
- Parallel execution MUST be used where possible
- Build caching MUST be implemented

## Security and Compliance

### Security Standards
#### Authentication and Authorization
- OAuth 2.0 / OIDC MUST be used for user authentication
- Service-to-service authentication via mTLS or JWT
- RBAC MUST be implemented at Kubernetes and application levels
- Principle of least privilege MUST be enforced

#### Data Protection
- Data at rest MUST be encrypted (AES-256 minimum)
- Data in transit MUST use TLS 1.3+
- Personally Identifiable Information (PII) MUST be identified and protected
- Data retention policies MUST be implemented and enforced

#### Vulnerability Management
- Automated scanning in CI/CD pipeline (Snyk, Trivy, or equivalent)
- Critical vulnerabilities MUST be patched within 7 days
- High vulnerabilities MUST be patched within 30 days
- Vulnerability disclosure process MUST be documented

#### Secrets Management
- Secrets MUST NEVER be committed to version control
- HashiCorp Vault or cloud provider secret managers MUST be used
- Secrets rotation MUST be automated
- Service accounts MUST use short-lived credentials

### Compliance
#### Audit Logging
- All authentication attempts MUST be logged
- All authorization failures MUST be logged
- All data access MUST be logged with user context
- Logs MUST be immutable and retained per compliance requirements

#### Regulatory Compliance
Projects MUST comply with applicable regulations:
- GDPR for EU user data
- SOC 2 for enterprise customers
- HIPAA for healthcare data (if applicable)
- PCI DSS for payment data (if applicable)

## Observability and Monitoring

### The Three Pillars
#### Metrics
- Prometheus MUST be used for metrics collection
- RED metrics MUST be implemented for all services:
  - Rate: Request rate
  - Errors: Error rate
  - Duration: Request duration
- USE metrics MUST be implemented for infrastructure:
  - Utilization
  - Saturation
  - Errors

#### Logging
- Structured logging MUST be used (JSON format)
- Log levels MUST be configurable per environment
- Correlation IDs MUST be propagated across service boundaries
- Log aggregation via ELK stack or cloud provider equivalents

#### Tracing
- Distributed tracing MUST be implemented via OpenTelemetry
- Critical paths MUST have trace sampling at 100%
- Non-critical paths MAY use adaptive sampling
- Trace context MUST be propagated through Kafka messages

### Alerting
#### Alert Design
- Alerts MUST be actionable (no "informational" alerts)
- Alerts MUST include runbook links
- Alert fatigue MUST be actively managed (max 10 alerts/week per team)
- Alert severity levels: Critical, Warning, Info

#### SLOs and SLAs
- Service Level Objectives (SLOs) MUST be defined for all production services
- Error budgets MUST be calculated and tracked
- SLA violations MUST trigger incident response
- SLO compliance MUST be reviewed monthly

## Documentation Requirements

### Mandatory Documentation
#### Code-Level Documentation
- Public APIs MUST have docstrings/JSDoc comments
- Complex algorithms MUST have explanatory comments
- TODO comments MUST include owner and date

#### Project Documentation
All projects MUST maintain:
- README.md with quickstart guide
- ARCHITECTURE.md with system design overview
- CONTRIBUTING.md with development guidelines
- CHANGELOG.md following Keep a Changelog format
- API documentation (generated from OpenAPI specs)

#### Operational Documentation
- Runbooks for common operational tasks
- Incident response procedures
- Disaster recovery plans
- Capacity planning documents

### Architectural Decision Records (ADRs)
#### ADR Requirements
Significant architectural decisions MUST be documented using ADRs containing:
- Context: Problem statement
- Decision: Chosen solution
- Consequences: Positive and negative impacts
- Alternatives: Rejected options and why

#### ADR Lifecycle
ADRs are immutable once accepted. New ADRs can supersede old ones but MUST reference them.

## Development Workflow

### Version Control
#### Git Workflow
- Trunk-based development with short-lived feature branches
- Branch naming: feature/, bugfix/, hotfix/
- Commit messages MUST follow Conventional Commits specification
- Force push is PROHIBITED on protected branches

#### Code Review
- All code MUST be reviewed before merging
- Minimum one approval required; two for critical changes
- Review checklist MUST be completed
- Automated checks MUST pass before review

#### Pull Request Standards
PRs MUST include:
- Clear description of changes and motivation
- Link to related specification or issue
- Test coverage for new code
- Updated documentation if applicable
- Screenshots for UI changes

### Release Management
#### Versioning
- Semantic Versioning MUST be used: MAJOR.MINOR.PATCH
- Breaking changes require MAJOR version bump
- New features require MINOR version bump
- Bug fixes require PATCH version bump

#### Release Process
1. Create release branch from main
2. Run full test suite
3. Generate changelog
4. Tag release with version
5. Deploy to staging
6. Execute smoke tests
7. Deploy to production (progressive rollout)
8. Monitor metrics and logs
9. Update release notes
10. Merge release branch back to main

#### Hotfix Process
- Hotfix branches created from production tag
- Fast-tracked review process (within 2 hours)
- Immediate deployment after passing tests
- Post-mortem required within 24 hours

## Performance and Scalability

### Performance Requirements
#### API Response Times
- P50 latency: < 100ms
- P95 latency: < 500ms
- P99 latency: < 1000ms
- Measurements exclude network transit time

#### Database Performance
- Query response time: < 50ms average
- Connection pool efficiency: > 90%
- Query cache hit rate: > 80%
- Index coverage: > 95% of queries

#### Message Processing
- Kafka consumer lag: < 1000 messages
- Event processing time: < 100ms per event
- Dead letter queue rate: < 0.1%

### Scalability Standards
#### Horizontal Scalability
- Services MUST be stateless to enable horizontal scaling
- Autoscaling MUST be configured based on CPU, memory, and custom metrics
- Maximum pod count MUST be defined to prevent runaway scaling

#### Load Testing
- Load tests MUST be executed before major releases
- Target load: 2x expected peak traffic
- Soak tests: 12 hours at expected peak traffic
- Chaos testing MUST be performed quarterly

## Cost Optimization

### Cost Monitoring
#### Resource Tagging
All cloud resources MUST be tagged with:
- Project name
- Environment (dev/staging/prod)
- Cost center
- Owner

#### Cost Tracking
- Monthly cost reviews MUST be conducted per project
- Cost anomalies (>20% increase) MUST trigger investigation
- Cost optimization opportunities MUST be documented and prioritized

### Efficiency Practices
#### Resource Right-Sizing
- Container resource requests MUST match actual usage (±20%)
- Database instances MUST be right-sized based on metrics
- Unused resources MUST be decommissioned within 30 days

#### Cost-Effective Patterns
- Spot instances for non-critical workloads
- Auto-scaling down during off-peak hours
- Data lifecycle policies for cold storage
- Reserved capacity for predictable workloads

## Governance

### Compliance Verification
#### Automated Checks
- Policy-as-code using Open Policy Agent (OPA)
- Admission webhooks for Kubernetes policy enforcement
- CI/CD gates for constitutional compliance
- Regular automated audits of all repositories

#### Human Review
- Architecture review board meets bi-weekly
- Quarterly compliance audits by security team
- Annual constitution review by engineering leadership

### Violations and Remediation
#### Violation Severity
- Critical: Security vulnerabilities, data loss risk
- High: Production reliability impact
- Medium: Technical debt, maintainability issues
- Low: Documentation gaps, minor deviations

#### Remediation Timelines
- Critical: Immediate action required, 24-hour resolution
- High: 7-day resolution
- Medium: 30-day resolution
- Low: Next sprint or quarterly cleanup

### Constitutional Amendments
#### Amendment Process
- Proposal submitted via RFC (Request for Comments)
- Community feedback period (minimum 2 weeks)
- Technical feasibility assessment
- Architecture review board approval
- CTO final approval
- Version bump and communication to all teams

#### Backward Compatibility
- Breaking changes require 6-month transition period
- Deprecation warnings MUST be issued
- Migration guides MUST be provided
- Legacy support maintained during transition

**Version**: 2.0.0 | **Ratified**: 2026-01-03 | **Last Amended**: 2026-01-03

## APPENDIX A: GLOSSARY
- ADR: Architectural Decision Record
- AIOps: Artificial Intelligence for IT Operations
- MCP: Model Context Protocol
- OPA: Open Policy Agent
- RFC: Request for Comments
- SLA: Service Level Agreement
- SLO: Service Level Objective
- SemVer: Semantic Versioning
