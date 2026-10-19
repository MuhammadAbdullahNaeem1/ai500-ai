# M1 · Practice answers Q1–100

Answers to the 100 short practice questions at the end of Module 1 (notes PDF page 151 onwards). These come from your Quiz 1 preparation guide, which was written from the Module 1 notes, your Assignment 1 report and your PA1 notebook — so definitions, lists and examples follow the notes' wording. Module 1 is examined again on the **mid**, and Module 2 builds on it (leakage, proxies, data quality).

<div class="pdf-links">
<a href="m1a-notes.html">Part A notes (1.1–1.4)</a>
<a href="m1b-notes.html">Part B notes (1.5–1.12)</a>
<a href="m1-cases.html">S, R and A answers</a>
<a href="pdfs/notes/Module-1-Notes.pdf#page=151">Questions in the PDF</a>
<a href="pdfs/quizzes/Quiz-1-Prep-Guide.pdf">Prep guide (PDF)</a>
</div>

:::note How to use
In the quiz, a strong short answer = **definition + reason + example from the notes**. Try each question first, then open the answer.
:::
## Questions 1–50


Each answer uses the notes' definitions and examples. In the quiz, a strong short answer = definition + reason + example from the notes.


### Historical and Philosophical Roots of AI

:::question Q1. Why is the history of AI better understood as a history of attempts to formalize intelligence rather than only as a history of faster computers?
:::solution Answer


Long before neural networks and GPUs, mathematicians, philosophers, engineers, psychologists, linguists and economists asked whether intelligence could be understood in formal terms, as rules, symbols, probabilities, algorithms or mathematical models. Each attempt to formalize intelligence (logic, probability, computation, information theory, feedback, cognitive science, optimization) contributed concepts that still shape AI even though the hardware changed. Faster computers only made it possible to run these formalizations; the core question was always: "Can perception, reasoning, learning, decision-making, and intelligent action be represented sufficiently precisely to be carried out by a machine?" So AI is "not a single invention" but a convergence of traditions.

:::
:::

:::question Q2. Identify the major intellectual traditions that contributed to the development of modern AI.
:::solution Answer

- formal logic and the mechanization of reasoning;
- probability and statistical inference;
- computation and algorithms;
- information theory (Shannon);
- control and feedback (Wiener's cybernetics);
- cognitive science and theories of intelligence;
- operations research and optimization;
- philosophy of mind, language, knowledge and agency.
:::
:::

:::question Q3. Explain how formal logic made the idea of mechanized reasoning possible.
:::solution Answer


Formal logic represents valid reasoning through formal symbols and rules. Once an argument is formalized, each step follows from explicit rules, so one can ask whether the steps can be executed mechanically without understanding. This idea led to symbolic AI, theorem proving, planning, expert systems, knowledge representation and logic programming. Its underlying position is that some forms of intelligence are "operations over structured representations", visible today in search over state spaces, planners applying operators, knowledge graphs and rule engines. Prolog is the classic example: it derives grandparent(tom, ann) from facts and a rule by mechanical proof.

:::
:::

:::question Q4. What does it mean to say that intelligence requires representation?
:::solution Answer


A machine "cannot reason directly about an unrepresented world". It can only reason over constructed representations: variables, symbols, vectors, tokens, states, graphs or probabilities. Whatever is not represented is invisible to it. Representation therefore decides which patterns and distinctions a system can learn or reason about (the same idea returns in Section 1.5.3, where representation is "the bridge between the physical world and computational models"). Related idea: a world model is an internal representation of how an environment works that lets an agent predict and plan.

:::
:::

:::question Q5. How does a symbolic program differ from a numerical program?
:::solution Answer


A numerical program (a calculator or a neural network) mainly manipulates continuous numbers and statistical weights. A symbolic program manipulates discrete symbols, logical structures and explicit rules to perform reasoning. It "does not understand the physical world; it only understands the representations it has been given." Example: a normal math library computes 2.5 × 2.5 = 6.25, while SymPy manipulates the symbols x and y themselves to prove that (x + y)² equals x² + 2xy + y².

:::
:::

:::question Q6. Explain how facts, rules, and queries interact in a Prolog program.
:::solution Answer

- Facts (knowledge representation): parent(tom, bob). parent(tom, liz). parent(bob, ann).
- Rules (formal logic): grandparent(X, Y) :- parent(X, Z), parent(Z, Y). The symbol :- means "is true if".
- Query (mechanized reasoning): ?- grandparent(tom, ann). asks "can you prove this?"

Prolog has no stored grandparent(tom, ann) fact. It searches its formal state space, matches the query against the rule, finds Z = bob that satisfies both parent facts, and mechanically deduces True. It does not know who Tom or Ann are.

:::
:::

:::question Q7. How does an expert system separate knowledge representation from the inference engine?
:::solution Answer


The knowledge (the rules) is stored separately from the reasoning engine (the code that applies them). In the notes' Python example, patient symptoms are stored as a set {"fever", "cough", "fatigue"}, and the medical rules are a list of if-then entries written by humans (for example {fever, cough, fatigue} → Flu). The inference engine, diagnose(), loops over the rules and checks whether each rule's conditions are a subset of the symptoms, returning the first match (output: Flu). Because they are separate, experts can change rules without changing the engine. The computer "does not discover these relationships. It simply follows them."

:::
:::

:::question Q8. How does symbolic theorem proving establish that two algebraic expressions are equivalent?
:::solution Answer


SymPy defines abstract symbols (x, y), builds symbolic expressions expr1 = (x + y)² and expr2 = x² + 2xy + y², and then mechanically simplifies their difference using formal algebraic rules (such as the distributive property). Because simplify(expr1 − expr2) reduces to the canonical form 0, the system has mechanically proven the expressions are equivalent. It does not understand the theorem like a mathematician; it has rules for manipulating expressions and checks whether both sides reduce to the same canonical form.

:::
:::

:::question Q9. Why is symbolic reasoning bounded by the symbols, facts, and rules supplied to the system?
:::solution Answer


The symbolic machine does not learn patterns from data; it only applies the rules it was given to the representations it was given. "If you do not provide the symbol, the fact, or the rule, the machine cannot reason about it." For example, the expert system returns "Unknown condition" for any symptom combination not in its rule list, and Prolog cannot prove a relationship it has no rule for. This is the lesson that "reasoning is just computation over structured representations", and it explains brittleness and the difficulty of acquiring and maintaining knowledge.

:::
:::

:::question Q10. Compare the roles of probability theory and statistical inference in reasoning under uncertainty.
:::solution Answer

- Probability theory provides the language for uncertainty. It starts from a known model or assumptions and works forward to the likelihood of outcomes (for example, "this patient has an 80% chance of the condition given the evidence").
- Statistical inference works in the opposite direction: from observed sample data to conclusions about an unknown population or parameters (for example, does this test reliably predict disease across thousands of patients?). It also separates observed patterns in a sample from population-level claims.

Together they changed the idea of intelligence from applying known rules to learning uncertain relationships from evidence, updating beliefs, quantifying confidence, and selecting actions under risk. Modern ML inherits this: parameters are estimated from data and predictions are "uncertain statements rather than infallible facts".

:::
:::


### Feedback, Information, and the Operational View of Intelligence

:::question Q11. How did cybernetics connect communication, feedback, and control in animals and machines?
:::solution Answer


Norbert Wiener's Cybernetics (1948) studied control and communication "in the animal and the machine". In a feedback system, the consequences of previous actions are observed (communication of information) and used to modify future behaviour (control). This treated intelligent systems as dynamic, adaptive and embedded in environments rather than isolated calculators. Examples: a thermostat correcting temperature, a robot adjusting its movement, a recommender learning from interactions, a fraud system changing thresholds, a reinforcement-learning agent adapting its policy through rewards.

:::
:::

:::question Q12. Explain how a feedback loop can make an AI system an active participant in the environment that it models.
:::solution Answer


Once predictions influence decisions, those decisions change the world, and the changed world produces the next training data. The data then reflect not just reality but also the system's earlier choices. In the predictive policing example, the model predicts high crime in an area, more police are sent, more minor incidents are recorded, and the new data "confirm" the prediction. "The model has changed the environment it is trying to predict." So AI systems are not passive observers; good design must consider how predictions reshape future data and outcomes.

:::
:::

:::question Q13. How can predictive policing produce self-reinforcing bias and selective labels?
:::solution Answer

- Historical data suggest a neighbourhood is high risk.
- The system sends more patrols there.
- More observation produces more recorded incidents.
- The new data reinforce the original prediction, and the model becomes more confident.

Self-reinforcing bias: the historical pattern is amplified each cycle. Selective labels: crime is only recorded where police were sent to look, so the data do not show crime in unpatrolled areas; the labels reflect where attention went, not the true underlying crime rate.

:::
:::

:::question Q14. Distinguish among self-reinforcing bias, selective labels, performative effects, and feedback loops.
:::solution Answer


| Term | Meaning |
|---|---|
| Self-reinforcing bias | Existing patterns in historical data become amplified over time. |
| Selective labels | Outcomes are observed only where the system directed attention (or for people it selected), not for the full population. |
| Performative effects | The prediction itself changes behaviour and creates conditions that make it appear accurate. |
| Feedback loops | The output of one prediction becomes part of the input for future predictions, potentially locking the system into a harmful cycle. |


The feedback loop is the mechanism; selective labels and performative effects are how it distorts the data; self-reinforcing bias is the result.

:::
:::

:::question Q15. Why is information not automatically equivalent to meaning?
:::solution Answer


Shannon showed that information can be measured and processed mathematically, so images, speech and text can all be encoded as data. But "a dataset may contain billions of values while failing to represent the phenomenon of interest." Meaning depends on how variables were defined, measured, collected, labelled and interpreted. A pixel value does not inherently represent happiness. So a model can find precise statistical patterns in the information that are nonetheless misleading about the real world.

:::
:::

:::question Q16. Use facial emotion recognition to explain how a dataset can contain abundant information but represent the target phenomenon poorly.
:::solution Answer


A face photo is millions of pixel values: plenty of information. But the meaning of the label depends on questions such as: How were emotions defined? Who labelled them? Were labels based on genuine feelings, facial expressions or human judgement? Did the data include diverse cultures, ages, lighting and contexts? If smiling faces are labelled "happy", the model learns smile = happiness, yet a smile can signal politeness, nervousness, discomfort or social expectation. The model can reach high accuracy on its dataset while misunderstanding human emotion. The three levels: information theory (pixels), machine learning (statistical relationships), meaning (what variables really represent).

:::
:::

:::question Q17. How did Claude Shannon contribute to concepts now used throughout machine learning?
:::solution Answer


His 1948 paper, A Mathematical Theory of Communication, formalized information, uncertainty, coding and transmission. It supplied concepts used throughout ML: entropy, cross-entropy (the standard classification loss), mutual information, compression, channel capacity and noisy communication. Its biggest consequence was that information became measurable and manipulable, so any signal (images, speech, text, sensor and biological data) could be encoded and processed as data.

:::
:::

:::question Q18. How did Alan Turing transform the question of machine thought into an operational evaluation problem?
:::solution Answer


In 1950 Turing replaced the vague question "Can machines think?" with an operational test based on observable interaction: can a machine's conversational performance become indistinguishable from a person's under specified conditions? This moved the focus from unverifiable metaphysical claims to measurable behaviour. AI evaluation is still operational: Can the system classify correctly? Solve a planning problem? Answer questions? Generate coherent text? Control a vehicle? Outperform a reference baseline?

:::
:::

:::question Q19. Why does successful performance on a Turing-style test not settle whether a machine understands?
:::solution Answer


Behavioural success does not answer the deeper questions: Does the system understand? Is it merely reproducing statistical regularities (the "stochastic parrots" concern)? Does intelligence require consciousness? Can linguistic performance be separated from grounding in the world? Should human-like behaviour be the standard? If thinking is defined as conscious experience rather than information processing, no amount of performance proves thought (Searle's argument). The notes separate "engineering tests of capability" from "philosophical claims about mind and understanding".

:::
:::

:::question Q20. What role did the Dartmouth proposal play in naming and consolidating the field of AI?
:::solution Answer


The 1955 proposal (McCarthy, Minsky, Rochester, Shannon) for the 1956 Dartmouth Summer Research Project used the term "artificial intelligence" and proposed studying whether learning and intelligence could be described precisely enough for machines to simulate them. Themes: language, abstraction, problem solving, self-improvement, neural mechanisms. It treated intelligence as decomposable into computational components and helped consolidate, name and legitimize the research traditions: symbolic reasoning, search and planning, machine learning, NLP, computer vision, robotics, knowledge representation and automated theorem proving.

:::
:::


### Symbolic AI, Statistical Learning, and Hybrid Systems

:::question Q21. State the main strengths of symbolic AI.
:::solution Answer


Explicit representations; inspectable reasoning chains; incorporation of domain rules; compositional structures; strong performance when the state space and rules are well specified (theorem proving, game playing, planning, expert systems). Newell and Simon argued physical symbol systems are central to intelligent action.

:::
:::

:::question Q22. State the main limitations of symbolic AI in complex and uncertain environments.
:::solution Answer


Difficulty acquiring and maintaining knowledge; brittleness under ambiguity; poor handling of noisy perception; combinatorial explosion; dependence on manually encoded representations.

:::
:::

:::question Q23. Why would a purely symbolic self-driving system struggle with ambiguity, noisy perception, and combinatorial explosion?
:::solution Answer


Rules such as "IF light is green THEN proceed" seem sufficient, but:

- Ambiguity: a pedestrian on the curb looking at a phone may or may not cross; the system needs a crisp symbolic state ("crossing" / "not crossing") that reality does not provide.
- Noisy perception: rain, fog, glare or a partly hidden sign can make perception mislabel a stop sign as a speed-limit sign; reasoning then starts from wrong symbols and can produce dangerous decisions.
- Combinatorial explosion: combinations of road conditions, weather, traffic density, pedestrian behaviour and vehicle interactions grow exponentially; rules for every combination are infeasible.
- Also: thousands of rules are needed for construction zones and emergency vehicles, and concepts like "safe following distance" must be hand-defined.

Hence real vehicles are hybrid: deep learning for perception, rules for traffic law, safety and high-level planning.

:::
:::

:::question Q24. State the main strengths of statistical machine learning.
:::solution Answer


Learning from high-dimensional observations; tolerance of noisy inputs; adaptation from examples; strong performance in perception, prediction and generation. The developer specifies a model class, objective, data representation and training procedure instead of programming every rule.

:::
:::

:::question Q25. State the main limitations of statistical machine learning.
:::solution Answer


Dependence on data quality; limited causal interpretation; potential opacity; vulnerability to distribution shift; difficulty guaranteeing behaviour outside the observed data regime.

:::
:::

:::question Q26. How can a pneumonia prediction model learn a hospital-specific shortcut rather than a medically meaningful pattern?
:::solution Answer


Severely ill patients are more likely to receive portable X-rays, so in the training data "portable X-ray" is strongly associated with pneumonia. The model can learn to predict from the image markers of the portable machine rather than from lung pathology. It predicts from correlation, not the medical cause (limited causal interpretation). At 98% test accuracy it looks ready, but at another hospital with different equipment and practices the shortcut no longer holds.

:::
:::

:::question Q27. What is distribution shift, and why can it reduce performance at a new hospital?
:::solution Answer


Distribution shift means the deployment data differ from the training data. A model trained on one hospital's X-ray machines, imaging protocols and patient demographics meets different machines, protocols and populations elsewhere; its learned relationships (including shortcuts) no longer match, so accuracy drops. Causes listed in 1.9.6: population changes, new devices, policy changes, seasonal effects, user adaptation, economic shocks, new clinical practice, adversarial behaviour, pipeline changes. Remedy: external validation and monitoring.

:::
:::

:::question Q28. Explain why symbolic AI and statistical machine learning should not be treated as a permanent binary choice.
:::solution Answer


Each has complementary strengths and weaknesses: statistical learning handles noisy perception but lacks guarantees and causal understanding; symbolic methods give explicit, inspectable rules but are brittle. Modern systems combine them: learned perception with rule-based constraints, neural representations with search, language models with retrieval, prediction with optimization, learned policies with safety controllers, and ML recommendations with human review. "The practical question is which representations and computational mechanisms are appropriate for the task."

:::
:::

:::question Q29. Describe how an autonomous warehouse robot can combine learned perception, search, optimization, safety rules, and human review.
:::solution Answer

- Learned perception: deep learning identifies shelves, packages, barcodes and people under varying light.
- Rule-based constraints: never exceed the speed limit, always stop for a person, never enter restricted zones.
- Neural representations with search: a network estimates traversable paths; a search algorithm finds the shortest safe route.
- Language models with retrieval: "where is item X?" is answered from the live inventory database.
- Prediction with optimization: forecast warehouse traffic and optimize routes to minimize delivery time and congestion.
- Learned policy with safety controller: an RL policy drives smoothly, but an independent controller overrides it when collision risk appears.
- Human review: for a damaged package the robot recommends discard or inspect; a supervisor decides.

A purely symbolic robot could not interpret noisy images; a purely statistical one might violate safety rules.

:::
:::

:::question Q30. Under what conditions is a hybrid AI system preferable to a purely symbolic or purely statistical system?
:::solution Answer


When the task has both (a) noisy, high-dimensional perception or patterns that are hard to hand-code (use learning) and (b) hard constraints, safety rules, legal requirements, or known domain logic that must always hold (use rules/search/optimization), and (c) high-stakes or ambiguous cases where accountability requires human review. Also when data are limited or shift over time and rules provide guarantees outside the observed data regime. Examples: autonomous vehicles, warehouse robots, clinical decision support, legal drafting with retrieval.

:::
:::


### Philosophical Questions, Agency, and Responsibility

:::question Q31. Why is intelligence better viewed as a spectrum of capabilities than as a single monolithic property?
:::solution Answer


No single definition covers every legitimate AI system. Intelligence includes many functional capacities: reasoning correctly, learning from experience, solving unfamiliar problems, using language, forming plans, acting toward goals, adapting, understanding context, interacting socially and creating artifacts. A route planner, an anomaly detector, a surgical robot and a language model each show different forms of computational competence. So it is more practical to characterize AI by which capabilities a system demonstrates.

:::
:::

:::question Q32. Compare prediction with causal reasoning.
:::solution Answer

- Prediction answers "What is likely to happen?" It exploits statistical associations, which may include shortcuts, proxies and dataset artifacts.
- Causal reasoning answers a counterfactual question: "What would happen if a specific intervention were applied?" It identifies cause-and-effect relationships and, following Pearl, requires explicit structural assumptions and mechanistic models, which cannot be derived from observational associations alone.

Accurate prediction identifies who is likely to succeed; causal reasoning determines which actions will actually improve success.

:::
:::

:::question Q33. Why can accurate prediction fail to answer a question about the effect of an intervention?
:::solution Answer


A predictor learns correlations in historical data, and those correlations may be driven by confounders or proxies rather than by the variable we would change. Intervening on the variable breaks the historical relationship. For example, a model predicting disease risk from hospital administrative markers, or student success from socioeconomic proxies, says nothing about what happens if we change those factors. The causal structure "generally cannot be derived from observational associations alone without additional assumptions or interventions" (for example randomized experiments). Also, both potential outcomes Y(1) and Y(0) are never observed for the same unit.

:::
:::

:::question Q34. Distinguish among counterfactual inquiry, structural assumptions, and mechanistic models.
:::solution Answer


| Concept | Asks / specifies | Notes example |
|---|---|---|
| Counterfactual inquiry | "What if we changed something?" | Would the student have passed if they had attended all lectures? Would crop yields rise with drip irrigation? |
| Structural assumptions | Which variables directly influence others (the causal pathways). | Smoking increases lung-cancer risk; rainfall influences crop production; traffic volume affects travel time. |
| Mechanistic models | How the process actually works to produce outcomes. | Weather model; pharmacokinetic model; epidemic model; traffic-flow model. |

:::
:::

:::question Q35. Use student attendance and exam performance to explain the difference between correlation and intervention effect.
:::solution Answer


A model finds that high-attendance students are much more likely to pass, and predicts well. But attendance may be a proxy for motivation, prior knowledge, study habits or family support. If the university made every student attend every lecture (an intervention), grades would not necessarily rise by the amount the correlation suggests, because disengaged students without prerequisites or study time would still struggle. Prediction: "Students with high attendance are likely to pass." Causal: "If we increase a student's attendance, how much will their probability of passing actually improve?"

:::
:::

:::question Q36. What does it mean to describe a deployed AI system as a socio-technical composite?
:::solution Answer


A deployed AI system is not just an algorithm. Its outputs are interpreted by people, built into workflows, and bounded by laws, resources, norms and incentives. Figure 4 shows five layers: Model, Data Infrastructure, Interface, Human Workflow, Institutional Rules. The same model can produce very different outcomes depending on the other four layers.

:::
:::

:::question Q37. Explain how data infrastructure, interface design, human workflow, and institutional rules can alter the impact of the same recruitment model.
:::solution Answer

- Model: learns patterns associated with successful applicants.
- Data infrastructure: training on past hiring decisions carries historical preferences for certain universities, locations or groups into the model.
- Interface: dashboards and ranked lists shape whether recruiters critically evaluate or simply accept the ranking.
- Human workflow: treating the score as final vs as a supporting recommendation produces different outcomes.
- Institutional rules: employment law, fairness policies and ethics standards decide how it is used and monitored.

"A technically accurate model may still create unfair hiring practices if the data, workflow, or governance mechanisms are poorly designed."

:::
:::

:::question Q38. Why should moral agency not be attributed directly to an algorithm?
:::solution Answer


An AI model "does not possess intent, judgment, or moral agency". It does not choose its training data, define its objectives, curate its labels, or decide where it is deployed. Operational parameters such as thresholds, confidence scores, human-review triggers and escalation policies are configured by developers and stakeholders. Every output reflects "a chain of human and institutional decisions". Blaming the algorithm hides who is actually accountable, so responsibility must be assigned to people across the lifecycle.

:::
:::

:::question Q39. How do upstream and downstream human decisions shape AI outcomes?
:::solution Answer

- Upstream (design, data collection, training): choosing training data, defining the objective (for example, maximize repayment), selecting features (location may act as a proxy), setting thresholds.
- Downstream (after deployment): how outputs are interpreted and acted on, whether loan officers treat recommendations as final, whether applicants can request review, how regulations monitor the system.

In the loan example the responsible questions are: Who selected the training data? Who defined success? Who approved deployment? Who monitored performance? What safeguards existed for affected people? So Responsible AI cannot be solved by "tweaking the code"; it needs governance across the whole lifecycle.

:::
:::

:::question Q40. Explain the Govern, Map, Measure, and Manage functions of the NIST AI Risk Management Framework.
:::solution Answer

- Govern: establish the culture, accountability structures and policies to manage AI risk (the bank assigns responsibility and creates policies).
- Map: identify and contextualize the specific risks of the system in its environment (unfair outcomes, privacy, impact on applicants).
- Measure: assess, analyze and track the risks with quantitative and qualitative metrics (accuracy, bias across groups, security, explainability).
- Manage: prioritize and act on risks by mitigating, transferring or accepting them (improve data, adjust processes, add human review, discontinue unsafe uses).

Goal: trustworthy AI that is valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed. Governance is cross-cutting, not a final checklist.

:::
:::


### The AI and Data Science Ecosystem

:::question Q41. Define artificial intelligence as both a scientific discipline and an engineering discipline.
:::solution Answer


Definition: "the scientific and engineering discipline concerned with constructing computational systems that perceive or receive information, form useful representations, reason or learn from evidence, and select actions or outputs in pursuit of specified objectives under uncertainty and constraints."

- As a science, AI studies: What is intelligence? How can knowledge be represented? How can a system infer conclusions from evidence? How can an agent learn? How should decisions be made under uncertainty? What resources does intelligent behaviour need?
- As engineering, it builds useful systems: recognizing objects, predicting risks, allocating resources, recommending content, detecting anomalies, generating content, planning routes, controlling machines, assisting decisions.

The distinction matters because a system can be useful without reproducing human cognition (a weather model need not think like a meteorologist).

:::
:::

:::question Q42. Compare systems that think like humans, act like humans, think rationally, and act rationally.
:::solution Answer

- Think like humans: reproduce human cognitive processes (memory, reasoning, perception); judged by whether the mechanism resembles human cognition. Roots in cognitive psychology, neuroscience, linguistics, philosophy of mind.
- Act like humans: judged only by observable behaviour; the Turing Test.
- Think rationally: formalize correct reasoning through logic (theorem proving, expert systems, constraint reasoning); limited because real environments are rarely complete or deterministic, so probability and decision theory are needed.
- Act rationally: a rational agent chooses actions expected to advance its objectives given information and constraints; handles uncertainty, incomplete information, limited computation, competing objectives, delayed consequences and exploration vs exploitation. Most useful for modern AI.
:::
:::

:::question Q43. What is a rational agent, and why does rational action not imply perfect action?
:::solution Answer


A rational agent "selects actions expected to advance its objectives, given its information and constraints." Rational means choosing the best action relative to what it knows and can compute, not the action that turns out best in hindsight. With uncertainty, incomplete information, limited computation, competing objectives and delayed consequences, even the best choice can have a bad outcome. "Rational action does not mean perfect action. It means selecting an appropriate action relative to the information, objectives, and resources available."

:::
:::

:::question Q44. Distinguish among passive analytical systems, decision-support systems, semi-autonomous systems, and autonomous systems.
:::solution Answer

- Passive analytical: turns data into insights or probabilities but cannot act (sales-forecast dashboard, disease-probability model, equipment-failure predictor).
- Decision-support: proposes specific actions; final authority and execution stay with humans (specialist-referral tool, ranking loans for underwriter review, maintenance priorities).
- Semi-autonomous: executes automatically in routine low-risk cases; escalates ambiguous or high-stakes cases (fraud blocking with borderline cases to investigators; screening that clears low-risk patients).
- Autonomous: perceives, decides and acts with little or no human intervention (manufacturing robots, warehouse sorting, high-frequency trading, closed-loop process control).
:::
:::

:::question Q45. Why should autonomy not be confused with intelligence?
:::solution Answer


Autonomy is about the authority and mechanism to act without human involvement; intelligence is about the capability to perceive, reason and learn. A thermostat acts autonomously in a narrow loop but has no general intelligence. A powerful language model may show strong linguistic reasoning but has no agency: it cannot act on the physical or institutional world without human mediation. So high autonomy does not imply intelligence, and high intelligence does not require autonomy. The level of autonomy should be set by risk, not by how clever the system is.

:::
:::

:::question Q46. Differentiate artificial intelligence, machine learning, data science, statistics, analytics, optimization, automation, generative AI, and data engineering.
:::solution Answer


Use Table 1 (Part 2, section 9). In one line each: AI is the broad umbrella for machines performing perception, reasoning, learning, planning, language, decision-making or adaptive action. ML is the major approach within AI that learns patterns or parameters from data. Data science is the broader lifecycle of acquiring, preparing, analyzing, modeling and communicating data, which may or may not use AI. Statistics is the inferential foundation: what can be inferred about a population from uncertain observations. Analytics is decision-oriented use of data (what happened, why, what may happen, what to do). Optimization finds the feasible choice that minimizes or maximizes an objective (used in training, planning, allocation, control). Automation executes a predefined process with limited human intervention and may contain no intelligence. Generative AI produces new content and is one family of AI capabilities, not all of AI. Data engineering builds the pipelines, schemas, stores, lineage and contracts on which data-driven AI depends.

:::
:::

:::question Q47. Why is machine learning not synonymous with artificial intelligence?
:::solution Answer


ML is only one subset of AI. Many robust, high-stakes AI systems operate without learning from data, using: search algorithms (state spaces, game trees); formal logic and automated reasoning; constraint satisfaction and mathematical optimization; automated planning and scheduling; knowledge bases and expert systems; manually engineered control rules. "Machine learning is merely one powerful methodology for achieving intelligent behavior, not the exclusive definition."

:::
:::

:::question Q48. Why is deep learning not synonymous with machine learning?
:::solution Answer


Deep learning is a specific class of ML defined by multi-layer artificial neural networks. Much of ML does not use deep networks: linear regression and kernel machines, decision trees and random forests, nearest-neighbour methods, Bayesian probabilistic models. "All deep learning is machine learning, [but] the vast majority of machine learning algorithms are not deep learning." (Your notebook's MLP is deep learning; your Bayes spam calculation is not.)

:::
:::

:::question Q49. Why is data science broader than model training?
:::solution Answer


Data science covers analytical, investigative and strategic activities. Its outputs include causal estimates and experimental designs (A/B tests, RCTs); exploratory analyses and data-quality investigations; statistical reports and visualizations; forecasting systems and operational ML models. "Model training is just one tool in the data scientist's toolkit"; the real scope is to extract, validate and communicate actionable knowledge from data.

:::
:::

:::question Q50. Compare the traditional emphasis of statistics with the traditional emphasis of machine learning.
:::solution Answer

- Statistics is rooted in inference: understanding the data-generating process. It emphasizes sampling and population inference, quantifying uncertainty and checking assumptions, estimation, identifiability and hypothesis testing. Example: an air-filter programme is evaluated with treatment and control neighbourhoods, estimation of the reduction, a hypothesis test, and a 95% confidence interval (15%, CI 10% to 20%).
- Machine learning is rooted in prediction: accurately mapping inputs to outputs. It emphasizes predictive performance and generalization, high-dimensional inputs and computational scalability, learned representations and automated function approximation. Example: tumour detection in 3D MRI with millions of voxels across many GPUs.

Breiman called these "the two cultures"; a mature practitioner combines both.

:::
:::


## Questions 51–100

:::question Q51. How do inferential thinking and predictive thinking complement each other in a mature AI project?
:::solution Answer


Predictive thinking (ML) delivers accurate mappings from inputs to outputs that generalize to unseen data. Inferential thinking (statistics) asks whether conclusions hold for the population, quantifies uncertainty, checks assumptions, and estimates effects of interventions. A mature project needs both: prediction to rank or flag cases, inference to check calibration and confidence intervals, test whether an intervention actually works (the air-filter study), and judge whether a sample represents the deployment population. Together they produce systems that are "not only highly accurate but also reliable, robust, and interpretable".

:::
:::

:::question Q52. Why is mathematical optimization ethically blind and epistemically blind?
:::solution Answer

- Ethically blind: it has no moral agency; it cannot evaluate fairness, justice or harm (for example, minimizing hiring cost by discriminating, or maximizing engagement by amplifying misinformation).
- Epistemically blind: it cannot judge whether its data and assumptions are valid: whether y is the correct target, whether the sample represents the deployment population, whether the loss reflects real harm, or whether the model should be deployed.

It just minimizes the empirical risk R̂(θ) = (1/n) Σ L(f_θ(x_i), y_i) it is given.

:::
:::

:::question Q53. Explain why optimization can solve a specified objective without validating whether the objective is appropriate.
:::solution Answer


The optimizer only sees the loss function and data; it does not know what the numbers mean. In the health-care example (Obermeyer et al.), the target was future health-care cost, assumed to be a proxy for health need. Because Black patients with the same illness historically generated lower costs (access barriers), the model learned they were lower risk and denied them care-management places. The optimization succeeded "brilliantly" at the specified objective while causing real harm. "Optimization solves the objective that was specified. It does not validate the objective." Validating the objective is the designers' responsibility.

:::
:::

:::question Q54. Distinguish automation without intelligence from intelligence without full automation.
:::solution Answer

- Automation without intelligence: a deterministic rule executes a task mechanically without reasoning. Legacy fraud script: "if a transaction exceeds \$10,000 and comes from a new IP address, freeze the account and send a rejection email". It cannot adapt to context, so a legitimate large purchase while travelling is blocked.
- Intelligence without full automation: an ML model analyzes hundreds of features (spending history, device fingerprint, geolocation, merchant risk) and outputs a nuanced assessment ("85% fraud, but matches this user's upcoming vacation"), then routes it to a human analyst who decides.

"Automation concerns how tasks are executed, whereas AI concerns how information is analyzed, patterns are inferred, and decisions are supported."

:::
:::

:::question Q55. Compare generative AI with discriminative AI and identify the distinctive risks of generative systems.
:::solution Answer

- Discriminative AI analyzes existing data to classify, rank, score or predict (a model flags risky clauses in 50,000 contracts).
- Generative AI learns the underlying distribution of data and synthesizes new outputs: text, images, audio, code (an LLM drafts a new NDA).

NIST Generative AI Profile risks: confabulation (hallucinated citations to non-existent cases); harmful content; information integrity (deepfakes, or a professional-looking draft accepted without verification); intellectual property and privacy (reproducing confidential settlement terms from training data); misuse (jailbreaking to produce exploitative clauses). Law firms therefore use discriminative models for low-risk high-volume tasks and heavy governance with mandatory human review for generative drafting.

:::
:::


### AI as an End-to-End Pipeline

:::question Q56. List and explain the eight stages of the end-to-end AI pipeline presented in the module.
:::solution Answer


1. Problem formulation: define the real-world decision, population, decision-maker, timing, outcome, baseline, error costs and constraints.


2. Data: acquire and prepare data while interrogating provenance, definitions, completeness, temporal integrity and governance; document with datasheets.


3. Representation: translate real entities into feature vectors, tensors, tokens, graphs or sequences; avoid loss of context, proxies, aggregation bias, leakage, identity errors and train-serving mismatch.


4. Model: learn f_θ: X → Y, chosen by data characteristics, task requirements, operational constraints, governance and lifecycle cost.


5. Evaluation: assess predictive performance (discrimination and calibration), fairness and robustness, operational viability and real-world impact; match tests to deployment claims; document in a Model Card.


6. Decision: turn p̂ into action with a threshold t set by error costs, capacity, uncertainty, fairness and human review; minimize C(t).


7. Deployment: embed into live infrastructure with latency limits, fallbacks, abstention, rollback, explanations and MLOps governance.


8. Monitoring: watch inputs, drift, pipelines, outputs, performance, operations, human interaction, fairness and feedback loops.

:::
:::

:::question Q57. Why should the AI pipeline be viewed as iterative and cyclical rather than as a one-directional waterfall?
:::solution Answer


Insights from later stages, especially monitoring, often reveal flawed assumptions, data drift or performance degradation. These trigger feedback to any earlier stage: re-collecting or relabelling data, engineering new representations, retraining, or even redefining the business problem. Real environments change, so a one-way process would lock in early mistakes. The figure shows "continuous feedback drives improvement" from monitoring back to problem formulation.

:::
:::

:::question Q58. What elements should a robust AI problem statement define before model development begins?
:::solution Answer


The target population and the decision-maker; the specific decision and the exact time it occurs; the desired outcome and available alternatives (including baseline/status quo); the consequences of errors (FP vs FN); and the operational and ethical constraints. In worksheet form: decision time, population/unit, available information, output, horizon, decision-maker, action, baseline, metrics, error costs, subgroup risks, constraints and governance. "If this statement cannot be completed clearly, model development should not begin."

:::
:::

:::question Q59. Why is the statement "build a model to predict hospital readmission" an inadequate problem formulation?
:::solution Answer


It is "vague, lacks operational context, and ignores the downstream impact". It does not say when the prediction is made (admission? discharge?), which patients are included, what counts as readmission (planned or unplanned) or within what window, who uses the output, what action follows, what resource is limited, what the baseline is, or which risks (calibration, subgroup fairness, false alerts) must be checked. Without these, features could leak, the model could be accurate but useless, and no one could judge success.

:::
:::

:::question Q60. What additional details make a hospital readmission problem operationally meaningful?
:::solution Answer


From the better framing: when (at the time of discharge); who uses it (the discharge team); what action (allocating follow-up appointments); what resource is constrained (a limited number of appointment slots); which patients (adult medical patients); what outcome period (unplanned 30-day readmission); what risks are examined (calibration, subgroup fairness, preventability and the consequences of false alerts).

:::
:::

:::question Q61. What questions should be asked about data provenance, variable definitions, completeness, temporal integrity, and governance?
:::solution Answer

- Provenance and purpose: Who or what produced the data, and for what original purpose?
- Definitions and proxies: Under which definitions were variables established? Which are direct measurements and which are proxies?
- Completeness and consistency: Which cases are missing? Was the outcome recorded consistently?
- Temporal and relational integrity: What has changed over time? Are timestamps reliable? Can records be linked correctly?
- Governance: Are the data legally and ethically permissible for this specific objective?
:::
:::

:::question Q62. What is the purpose of a Datasheet for Datasets?
:::solution Answer


Proposed by Gebru et al. and inspired by electronics datasheets, it documents a dataset's motivation, composition, collection methods, preprocessing steps, recommended uses and limitations. It makes implicit assumptions, biases and constraints explicit, so developers and downstream users understand the data's boundaries, reduce misuse, and build on "a foundation of transparency and informed consent".

:::
:::

:::question Q63. How can poor dataset documentation lead to unsafe deployment of a skin lesion classifier?
:::solution Answer


The 100,000-image dataset was about 90% fair-skinned patients, mostly from specialized clinics in one country, captured with high-end clinical cameras (while many hospitals use smartphones), and labelled by single dermatologists without verification. None of this was documented, so developers assumed it was representative and hospitals adopted it. Months later it performed much worse for darker skin. A datasheet listing these limitations ("underrepresentation of darker skin tones, children, and smartphone images; not validated for primary care") would have prompted more data collection, fairness evaluation, or restricted deployment.

:::
:::

:::question Q64. Why is representation described as the bridge between the physical world and computational models?
:::solution Answer


Algorithms cannot process people, images, documents or road networks directly; representation translates them into structured mathematical forms: a person into a feature vector, an image into a tensor of pixel intensities, text into tokens or embeddings, a road network into a graph, purchases into an event sequence, a physical process into a state-space model, categories into one-hot or learned embeddings. Representation "dictates exactly which information is visible to the model", so it determines which patterns are easy or hard to learn.

:::
:::

:::question Q65. Explain loss of context, proxy encoding, aggregation bias, temporal leakage, identity errors, and train-serving mismatch.
:::solution Answer


See Part 2, section 13 for the table. Short versions with the ICU sepsis example:

- Loss of context: a 24-hour average heart rate hides a dangerous spike one hour ago.
- Proxy encoding: home zip code encodes socioeconomic status and race, so alerts are deprioritized for marginalized neighbourhoods.
- Aggregation bias: 92% overall accuracy hides failure for paediatric and autoimmune patients.
- Temporal leakage: antibiotic dose counts updated after the diagnosis let the model "wait for the doctor's order" (99% test accuracy, fails live).
- Identity errors: a transferred patient split into two IDs, hiding the deterioration trend.
- Train-serving mismatch: missing BP imputed with the ward median in training but with 0 in production, flooding nurses with false alarms and causing alert fatigue.
:::
:::

:::question Q66. What does the mapping f_θ: X → Y represent in model development?
:::solution Answer


A model is a mathematical function that maps structured input representations X (the feature space) to outputs Y (predictions or decisions), with parameters θ learned from data. It can be a linear function, decision tree, nearest-neighbour procedure, probabilistic graphical model, deep network, search or optimization program, rule set, or a neuro-symbolic hybrid. Optimization is not guaranteed to find the global optimum; it may reach a local, approximate or regularized solution.

:::
:::

:::question Q67. Which operational, governance, data, and lifecycle criteria should guide model selection?
:::solution Answer

- Data characteristics: size, dimensionality, nonlinearity.
- Task requirements: classification, regression, ranking; need for probabilistic calibration.
- Operational constraints: latency, memory, computational limits for real-time inference.
- Governance and trust: interpretability, explainability, robustness required by stakeholders or regulators.
- Lifecycle costs: long-term maintenance burden and ML expertise available in the team.

"The choice should never be based on hype."

:::
:::

:::question Q68. Why can a simpler model be preferable to a more accurate but complex model?
:::solution Answer


Loan example: DNN 94% accuracy vs logistic regression 91% with 15 features. The simpler model wins because: interpretability (ECOA requires specific adverse-action reasons; logistic coefficients give them directly, while post-hoc SHAP on a DNN can be unstable); data size (50,000 applications a year is too small for a massive DNN without overfitting); maintenance cost (after economic shifts, standard risk analysts can maintain logistic regression, while a DNN needs specialized ML engineers); latency and compute (logistic regression runs on cheap CPUs). A slightly less accurate model that fits the constraints delivers more real-world value.

:::
:::

:::question Q69. Why should the principle of parsimony be treated as a heuristic rather than as a rule that reality must always be simple?
:::solution Answer


Occam's principle says prefer the simplest model only when competing explanations fit the evidence equally well. It does not claim reality is simple. A physician who insists that tuberculosis alone explains cough, fever, weight loss and joint pain misses coexisting rheumatoid arthritis and delays treatment. Because the two-disease model fits the evidence better, it is the right choice despite being more complex. Parsimony should "encourage avoiding unnecessary complexity, not ignoring necessary complexity."

:::
:::

:::question Q70. What information should a Model Card communicate to downstream users?
:::solution Answer


Following the notes' heart-disease Model Card: Model Overview (name, purpose, type, architecture, intended use); Data Description (data source, features, preprocessing such as mean/mode imputation, exclusions such as race or genetics); Performance Metrics (overall accuracy, precision, recall, F1, performance by subgroup, fairness observations); Known Limitations (bias in data, generalizability, feature limitations); Intended and Inappropriate Uses; Ethical Considerations (fairness, impact of misuse); Additional Considerations (future work). Section 1.5.5 summarizes the purpose: record the intended use, evaluation procedures, conditions under which it performs well, detailed subgroup results and known limitations, giving users "a clear, honest picture of the system's capabilities and boundaries". (A complete example is in A2, Part 8.)

:::
:::


### Evaluation, Decisions, Deployment, and Monitoring

:::question Q71. Why is overall accuracy insufficient for evaluating a high-stakes AI system?
:::solution Answer


Accuracy treats all errors as equally costly and can hide: poor calibration (80% predicted risk but 45% observed deterioration in the ED triage example); subgroup failures (lower accuracy for elderly and non-English speakers); fragility (crashing when one vital sign is missing); operational problems (15-second latency, worse on night shifts); and lack of real-world benefit (only 2% better than the existing early warning score, and alert fatigue destroyed decision utility). It is also misleading with class imbalance. The real question is whether the system is "sufficiently reliable, safe, and effective for its specific intended use".

:::
:::

:::question Q72. Distinguish discrimination from calibration.
:::solution Answer

- Discrimination: the model's ability to separate or rank positive cases above negative ones (measured by AUROC).
- Calibration: whether predicted probabilities match observed frequencies; a predicted 80% risk should correspond to about 80% observed events.

A model can discriminate well yet be badly calibrated (readmission example: ranks well, but 80% predicted means 35% observed). Calibration matters whenever the probability itself is used for decisions or resource allocation.

:::
:::

:::question Q73. What evaluation dimensions should be assessed in addition to predictive performance?
:::solution Answer

- Fairness and robustness: subgroup performance, robustness to noise and distribution shift, interpretability.
- Operational viability: computational cost, inference latency, stability across times, environments and sites.
- Real-world impact: decision utility, comparison with meaningful baselines, and human-system performance (how humans and AI perform together).
:::
:::

:::question Q74. Why must temporal, geographic, equity, probabilistic, and decision claims be matched with appropriate validation methods?
:::solution Answer


Because a test only supports the claim it actually checks. Readmission example:

- Temporal claim: random 80/20 split gave 85%; training on 2022 and testing on January 2023 gave 68%, exposing a billing code used only for three months in 2021.
- Geographic claim: strong at the urban flagship; external validation at rural clinics failed because a lab test only existed at the flagship.
- Equity claim: AUC 0.82 overall but 0.55 for non-English speakers.
- Probabilistic claim: calibration curve showed 80% predicted vs 35% observed.
- Decision claim: a prospective pilot showed 60% flagged, alert fatigue, and nurses reverting to spreadsheets.

"How you test an AI is just as important as what you test."

:::
:::

:::question Q75. Why is a machine learning prediction not the same as a decision?
:::solution Answer


A model outputs a probability p̂ = P̂(Y = 1 | X = x); a decision requires a concrete action. Converting one to the other requires a decision rule (intervene if p̂ ≥ t) whose threshold reflects error costs, intervention capacity, uncertainty, fairness and human review. The same prediction can lead to different actions under different capacities or values. "A prediction is just a number; the decision is where human values and operational constraints are actually applied."

:::
:::

:::question Q76. How should asymmetric error costs, intervention capacity, uncertainty, fairness, and human review influence a decision threshold?
:::solution Answer


Rapid Response Team example:

- Asymmetric costs: a missed deterioration (FN) can mean a preventable death while a false activation (FP) costs a brief assessment, so t is pushed below 0.5.
- Intervention capacity: only two RRT nurses at night; t = 0.2 might flag 40 patients, so t is raised enough to stay within capacity.
- Uncertainty and expected benefit: for borderline p̂ (0.35 to 0.45) trigger a lower-acuity action (more frequent vital-sign checks) instead of a full activation.
- Fairness: a single global t gave a high FN rate for non-English speakers; recalibrate, improve data, retrain, or where appropriate adjust thresholds.
- Human-in-the-loop: a two-minute nurse review before dispatch allows a lower t (0.3) if false positives stay manageable.

The threshold is a "tunable policy lever", not a mathematical default.

:::
:::

:::question Q77. Interpret the conceptual decision-cost function that combines false positives, false negatives, delay, and workflow cost.
:::solution Answer


C(t) = c_FP·P(FP|t) + c_FN·P(FN|t) + c_delay·E[D|t] + c_workflow(t)


The system chooses the threshold t that minimizes total real-world cost: the cost of false alarms times their probability, the cost of misses times their probability, the cost of expected delay or friction, and the cost of fitting the threshold into the human workflow. Lowering t reduces misses but increases false alarms, queues and workload. Baggage example: t = 0.4 maximized accuracy (96%) but created huge manual-search queues and broke the two-station checkpoint; t = 0.7 (94% accuracy) minimized C(t). "The optimal decision threshold is rarely the one that simply maximizes overall accuracy."

:::
:::

:::question Q78. What engineering and governance questions must be answered before moving a model from a sandbox into production?
:::solution Answer

- Infrastructure and performance: Where will inference occur (cloud, edge, on-premise)? What is the maximum latency? Which features are actually available in real time?
- Resilience and failure handling: What happens when inputs are missing, delayed or corrupted? Can the system abstain? What is the fallback? Can it be rolled back instantly?
- Human-system interaction: Who receives the output? How are reasoning and uncertainty explained?
- Governance and MLOps: How are model versions, code and pipelines controlled and tracked? Who is accountable for monitoring, retraining and maintenance?
:::
:::

:::question Q79. What is the role of abstention, fallback procedures, rollback mechanisms, and circuit breakers in deployment?
:::solution Answer


They make the system fail safely. Abstention: the model declines to predict when confidence is too low and defers to a human or another process. Fallback: a defined safe path when inputs are missing or errors occur (in the fraud example, a missing geolocation feature routes the transaction to the legacy rule-based system). Rollback: reverting instantly to a previous stable version. Circuit breaker: an automatic trigger for rollback; if the decline rate spikes more than 5% in 10 minutes, the system rolls back to protect legitimate customers.

:::
:::

:::question Q80. What should be monitored across input quality, drift, feature pipelines, model outputs, predictive performance, operations, human interaction, fairness, and feedback loops?
:::solution Answer

- Input quality: missing values, invalid ranges, unexpected formats, schema changes (an app update alters telemetry).
- Input distribution (data drift): shifts in demographics, devices, regions, language, case mix.
- Concept and label drift: changing relation between inputs and outcomes (fraudsters change tactics).
- Feature pipelines: transformation errors, delayed joins, missing updates, stale features.
- Model outputs: prediction distributions, confidence, uncertainty, abstention rates.
- Predictive performance and ground truth: error rates, calibration, precision, recall, F1, subgroup metrics; availability and timeliness of labels.
- Operational health: latency, uptime, throughput, CPU/GPU/memory.
- Human-system interaction: override rates, acceptance, corrections, automation bias.
- Harm, fairness and safety: unequal error rates, harmful outcomes.
- Feedback loops: predictions shaping future training data.
:::
:::


### Types of AI Problems

:::question Q81. Distinguish binary, multiclass, and multilabel classification.
:::solution Answer

- Binary: Y ∈ {0, 1}; fraud vs legitimate, disease vs no disease, spam vs non-spam.
- Multiclass: Y ∈ {1, …, K}; exactly one class is chosen (handwritten digit).
- Multilabel: Y ⊆ {1, …, K}; several labels may apply at once (several diagnoses on one clinical record).
:::
:::

:::question Q82. Why must a classification label such as "high risk" include an event definition, threshold, and time horizon?
:::solution Answer


"High risk" alone is not operationally meaningful: high risk of what event, how high, and by when? Without an event definition the label cannot be measured consistently; without a threshold nobody knows which scores count as high; without a horizon the prediction cannot be matched to an intervention window. Example: "unplanned readmission within 30 days, p̂ ≥ t" (or in RYDA, not in verified employment at day 180 and ranked in the top 300).

:::
:::

:::question Q83. Compare mean squared error and mean absolute error for regression tasks.
:::solution Answer


L_MSE(y, ŷ) = (y − ŷ)²     L_MAE(y, ŷ) = |y − ŷ|


MSE squares errors, so it penalizes large errors heavily (useful when big misses are dangerous). MAE grows linearly, so it is more robust to large deviations and outliers. The choice "encodes an assumption about error".

:::
:::

:::question Q84. Why should the regression loss function reflect the real application rather than convention alone?
:::solution Answer


The loss defines what the model treats as a bad mistake. If real harm grows sharply with error size (under-predicting energy demand causing blackouts), MSE fits; if outliers are noise, MAE fits; if over- and under-prediction have different costs (asymmetric cost), neither symmetric loss is right. Table 2 lists ignoring skew, heteroscedasticity or asymmetric cost as the common regression framing error. Choosing by habit optimizes the wrong thing (optimization is blind to whether "the loss function reflects real harm").

:::
:::

:::question Q85. How do ranking and recommendation differ from ordinary classification?
:::solution Answer


Ranking produces an ordered list and is evaluated by list-aware metrics (NDCG, MAP, precision@k); items cannot be judged independently of their position. Recommendation adds personalization and availability constraints (recall@k, NDCG, utility, diversity). Crucially, a recommender "selects what the user will be shown", influencing future preferences and creating the feedback loop: past exposure → observed interaction → training data → future exposure. Ordinary classification labels items independently and does not choose what data it will see next.

:::
:::

:::question Q86. Why are observed clicks not pure measures of user preference in a recommendation system?
:::solution Answer


Clicks are "conditional on previous rankings, interface design, position, and availability". Users can only click what they are shown, and items shown near the top get more clicks regardless of quality (position bias). Those clicks then become training data, so the system learns its own past choices (selective exposure, feedback loop). Optimizing clicks can also differ from long-term benefit.

:::
:::

:::question Q87. Why should clusters not automatically be treated as objectively real categories?
:::solution Answer


Clustering finds structure without labels, and the result depends on the representation, scaling, algorithm and number of clusters. "A mathematically compact partition may still be scientifically meaningless." So clustering requires stability analysis, sensitivity to representation and scaling, inspection of cluster composition, domain validation, and caution against reifying algorithmic groups as natural categories (for example, customer segments are useful summaries, not natural kinds).

:::
:::

:::question Q88. What components are required to formulate a search problem?
:::solution Answer


An initial state, actions or transitions, a goal test, a path cost, and possibly a heuristic (a problem-specific estimate that guides search toward the goal, such as straight-line distance in A*). The common framing error is defining an incomplete search space.

:::
:::

:::question Q89. Compare search, planning, and control as classical AI problem types.
:::solution Answer

- Search explores a space of states or candidates to find a goal state, path or document (route finding, document retrieval); evaluated by relevance, path cost, success rate, latency.
- Planning identifies a sequence of actions expected to achieve a goal while satisfying constraints (robot task planning); error: assuming a static or fully known environment.
- Control repeatedly observes a system and acts over time: x_{t+1} = F(x_t, u_t, w_t), with state x, action u and disturbance w (keeping a drone on its trajectory); evaluated by stability, tracking error, safety, energy. "Unlike static prediction, control changes the process being predicted."
:::
:::

:::question Q90. Explain the main framing risks in anomaly detection, generation, forecasting, causal estimation, and decision optimization.
:::solution Answer

- Anomaly detection: "unusual is not the same as undesirable"; anomalies may be fraud or legitimate novelty; without an investigation or response policy it only produces unusualness scores (error: assuming all rare cases are harmful).
- Generation: a fluent output can still be false, unsafe, biased or irrelevant; evaluate plausibility, grounded correctness, and utility and safety (error: equating fluency with truth).
- Forecasting: time order matters; random splits leak the future; use temporal holdouts or rolling-origin validation, compare with naive or seasonal baselines, and watch for trend, seasonality, autocorrelation and structural change.
- Causal estimation: τ = E[Y(1) − Y(0)] but both outcomes are never seen for the same unit; needs randomization, exchangeability, positivity, consistency, correct temporal ordering and control of confounding (error: interpreting correlation as intervention effect).
- Decision optimization: a* = argmax E[U(a, Y) | X = x]; errors include optimizing an incomplete proxy objective, treating risk as intervention benefit, ignoring constraints, and evaluating predictions without evaluating the resulting actions.
:::
:::


### Problem Formulation and Common Failure Modes

:::question Q91. Why should an AI project begin with a decision or capability rather than with an available dataset?
:::solution Answer


The data-first trap (grab a convenient dataset, pick an interesting target, maximize AUC, then look for a use case) produces "highly accurate mathematical curiosities that deliver zero real-world value". Attrition example: an 88%-AUC model listed 500 at-risk employees, but HR had no budget or time to act and the model was abandoned. Starting from the decision (which employees should managers target, with only five interventions per quarter) led to a transparent heuristic that caught 80% of churners and was trusted and used. "A model that does not change a decision or trigger a concrete action has zero operational value."

:::
:::

:::question Q92. What questions are included in a comprehensive problem-framing canvas?
:::solution Answer

- The Decision: What specific decision will be altered, informed or automated?
- The Actor: Who is the decision-maker responsible for executing it?
- The Actions: What concrete interventions are available once the output is generated?
- The Necessity of AI: Is a complex ML model actually required?
- The Simpler Alternatives: Could a deterministic rule, checklist, statistical summary or process redesign do it more cheaply or reliably?
:::
:::

:::question Q93. Define the target population, unit of analysis, index time, prediction horizon, inputs, outputs, labels, constraints, stakeholders, and cost of error.
:::solution Answer

- Target population: the set of cases the system is meant for, with inclusion and exclusion criteria (adult medical patients).
- Unit of analysis: the independent entity being predicted for: individual, event, object or spatial entity.
- Index time: the exact moment the prediction is made.
- Prediction horizon: the future window in which the outcome must occur.
- Inputs: documented features (definition and source, unit, update frequency, missingness, timestamp semantics, availability at inference, privacy class, transformation, known biases).
- Outputs: class, value, probability, interval, ranking, score, tier, recommendation, action, artifact, or abstention.
- Labels: the ground truth used for training, often a proxy that must be interrogated.
- Constraints: technical, resource, trust and usability, governance and legal boundaries.
- Stakeholders: subjects, targets, operators and experts, and the broader ecosystem.
- Cost of error: the real consequences of TP, FN, FP, TN, which are usually asymmetric and include non-financial harms.
:::
:::

:::question Q94. Why must every feature be available at or before the index time?
:::solution Answer


Because the deployed model can only use what is known at the moment it predicts. A feature recorded later carries future information; it looks very predictive in retrospective data but is unavailable (or different) in real time. "Using that result does not constitute early prediction; it is merely hindsight." This is target/temporal leakage: "If a model relies on data that has not yet occurred at the index time, it is leaking the future, not demonstrating intelligence." Data engineering must also check availability, not just event time: t_feature availability ≤ t.

:::
:::

:::question Q95. How should a project team define a meaningful baseline and an evaluation plan before training begins?
:::solution Answer


Baseline: the real alternative the system will replace or augment, not random guessing: current professional judgment, a simple heuristic, the status quo, a legacy system, or alternative policies (for example random allocation). The question becomes "Does deploying this AI system improve real-world outcomes compared to the best available alternative?"


Evaluation plan (locked before training): primary and secondary (guardrail) metrics; validation strategy (external, temporal and prospective testing); reliability and fairness (subgroup analysis, calibration, uncertainty, robustness); operationalization and governance (decision thresholds, acceptance criteria, monitoring plan). Locking it in prevents metric shopping and data dredging: "An evaluation plan written after the fact is merely a retrospective justification for deployment."

:::
:::

:::question Q96. Explain how solving the wrong problem, poor data quality, data leakage, weak evaluation, underspecification, distribution shift, ignored workflow, and absent monitoring can cause AI failure.
:::solution Answer

- Wrong problem: the target is disconnected from the goal (predicting cost instead of preventable illness; clicks instead of welfare; risk with no capacity to act).
- Poor data quality: wrong values, missing records, inconsistent units, duplicate identities, delayed updates, coding changes, unrepresentative samples, unreliable labels, undocumented preprocessing; more data does not fix systematic bias.
- Data leakage: target, temporal, group, preprocessing, label leakage and benchmark contamination give unusually impressive but fake results.
- Weak evaluation: only accuracy, convenient test sets, ignored imbalance, test-set tuning, no CIs, no baseline, no calibration, no subgroups, random splits for temporal use.
- Underspecification: several models with equal test scores rely on different shortcuts and behave differently under shift; mitigate with stress tests, multiple runs, shift and subgroup evaluation, causal checks.
- Distribution shift: populations, devices, policies, seasons, users, economy or pipelines change.
- Ignored workflow: alerts too late, distrust, poor explanations, too many alerts, automation bias, unclear responsibility, infeasible actions, more workload.
- No monitoring: silent degradation when schemas change, features fail, labels are delayed, thresholds change, new subpopulations appear, or versions are not recorded.
:::
:::


### Data Engineering and Illustrative Case Studies

:::question Q97. Why is data engineering described as the connective tissue of the complete AI lifecycle?
:::solution Answer


Every stage depends on data flowing reliably: generated, captured, validated, stored, transformed, served, observed and governed. Every model needs data with defined meaning, delivered consistently to training and production; labels and outcomes must be linked over time; behaviour must be monitored; decisions audited; privacy enforced; source changes detected; failures made reproducible and reversible. So data engineering is "not merely what happens before machine learning"; it connects problem formulation to monitoring. "Reliable model ⇏ Reliable AI system."

:::
:::

:::question Q98. How do semantics, temporal correctness, training-serving consistency, lineage, governance, and monitoring make data engineering unavoidable?
:::solution Answer

- Semantics: "temperature" needs units, site, sensor, timestamp, missing code and calibration status; "diagnosis_date" could mean symptom onset, documentation, confirmation, entry or billing date.
- Temporal correctness: features must be recorded and available by prediction time (t_feature availability ≤ t); no train/test overlap; no stale data treated as real time.
- Training-serving consistency: encodings, missing-value handling, units, windows, library versions and batch vs streaming must match; use shared versioned transformations and tests.
- Lineage: source version, query, transformation code, label definition, partitions, seed, libraries, configuration, evaluation data, approval and deployment version, for audit and rollback.
- Governance: role-based access, encryption, retention limits, de-identification, consent tracking, audit logs, purpose restrictions, deletion workflows, incident response.
- Monitoring: only possible if inputs, predictions, versions, human responses, outcomes and subgroup data are captured.
:::
:::

:::question Q99. What lessons about proxies, drift, lineage, and ground-truth anchoring can be learned from Google Flu Trends and the Epic Sepsis Model?
:::solution Answer


Google Flu Trends: search behaviour ≈ disease activity is only a proxy, affected by media, anxiety, platform design and habits. It overestimated flu in 100 of 108 weeks and exceeded CDC estimates by more than 2× in February 2013. Causes: big-data hubris (about 50 million candidate terms against 1,152 weekly observations, chance correlations) and algorithm dynamics (the platform changed the data-generating process). Lessons: volume does not remove measurement bias; a proxy is useful only while its relationship to the target is stable; platforms are part of the data-generating process; undocumented term lists destroy reproducibility (lineage); combining GFT with lagged CDC data cut MAE to 0.232 (vs 0.486 and 0.311), so new sources should complement ground truth; monitor residual drift and suspend when it grows.


Epic Sepsis Model: external validation (38,455 hospitalizations) found AUROC 0.63, alerts on 18% of hospitalizations, 67% of sepsis cases missed at threshold ≥ 6, and only 183 cases caught before timely antibiotics. Lessons: the label must match the intended clinical event (labels built from clinician actions encode practice); timing is as important as accuracy (predicting after antibiotics are ordered is useless); features need event, recording, availability and correction times; missingness encodes clinician behaviour; sites differ, so external and prospective validation are essential; alert volume is a system-level metric; workflow decides value.

:::
:::

:::question Q100. How does TensorFlow Extended demonstrate that production AI depends on ingestion, statistics, schemas, validation, transformation, training, evaluation, model validation, serving, monitoring, and lineage?
:::solution Answer


TFX turns a one-off training script into a repeatable pipeline: ingestion with versioned specs, record counts and checksums; statistics on distributions, missingness, ranges and label balance; a schema that makes assumptions machine-checkable; data validation catching missing columns, new categories and shifts; transformations defined once for training and serving (no skew); training that records code, data, hyperparameters and seeds; evaluation against the current production model; model validation that blocks release if metrics, subgroup performance, fairness or latency fail; serving and monitoring with version metadata and rollback. Remove any piece and reliability drops (silent corruption, skew, irreproducible results, worse models shipped, invisible failures). Business value (months to weeks deployment; about 2% more Google Play installs) came from the whole system. "Data engineering ... constitutes much of the production architecture."

:::
:::
