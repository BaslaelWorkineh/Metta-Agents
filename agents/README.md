# MettaAgents Framework

A powerful and flexible agent-based system implemented in MeTTa, designed for cognitive architectures and distributed AI systems.

## Overview

MettaAgents is a framework that implements various cognitive agents using the MeTTa language. The system is built on a robust architecture that allows agents to operate independently or in parallel, with sophisticated mechanisms for message passing and state management.

## Core Components

### Base Architecture

- `AgentObject`: The foundational class that enables both MeTTa scripts and Python classes to function as agents
- `BaseListeningAgent`: An extension that adds message processing and event handling capabilities
- `ParallelScheduler`: Manages the concurrent execution of multiple agents

### Available Agents

1. **Importance Diffusion Agents**
   - `AFImportanceDiffusionAgent`: Implements attention flow-based importance diffusion
   - `WAImportanceDiffusionAgent`: Handles weighted attention-based importance diffusion

2. **Rent Collection Agents**
   - `AFRentCollectionAgent`: Manages attention flow-based resource allocation
   - `WARentCollectionAgent`: Handles weighted attention-based resource collection

3. **Learning and Memory Agents**
   - `HebbianCreationAgent`: Implements Hebbian learning for pattern creation
   - `HebbianUpdatingAgent`: Manages updates to Hebbian learning patterns
   - `ForgettingAgent`: Handles memory decay and cleanup operations

## Key Features

- **Parallel Execution**: Agents can run concurrently using the ParallelScheduler
- **Message Queue System**: Built-in message passing infrastructure for inter-agent communication
- **Event Handling**: Robust event processing system for reactive behaviors
- **Flexible Integration**: Supports both MeTTa and Python-based agent implementations

## Usage

### Creating an Agent

Agents can be created either through MeTTa scripts or Python classes:

```metta
;; MeTTa agent example
!(bind! agent (new-agent))
```

### Registering with Scheduler

```python
scheduler = ParallelScheduler()
scheduler.register_agent("agent_id", agent_creator)
```

### Running Agents

```python
# Run a single agent
scheduler.execute_agent("agent_id")

# Run all agents in parallel
scheduler.run_all_agents_parallel()
```

## Architecture Details

### Agent Lifecycle

1. **Initialization**: Agents are initialized with optional path, atoms, and include paths
2. **Registration**: Agents are registered with the scheduler
3. **Execution**: Agents process messages and handle events in their main loop
4. **Termination**: Agents can be gracefully stopped using the stop method

### Message Processing

Agents use a queue-based system for message processing:
- Messages are added to the queue using the `input` method
- The `message_processor` handles incoming messages
- The `messages_processor` runs continuously while the agent is active

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

[Insert License Information]
