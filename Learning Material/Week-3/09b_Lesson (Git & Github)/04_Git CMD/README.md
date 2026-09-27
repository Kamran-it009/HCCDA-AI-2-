# **Basic Git Commands**

---

#### **1. `git init`**
- **Purpose:** Initializes a new Git repository.
- **Usage:**
  ```bash
  git init
  ```
  This will create a `.git` directory in your current folder, which tracks your project’s changes.

---

#### **2. `git clone`**
- **Purpose:** Clone an existing repository from a remote location (like GitHub) to your local machine.
- **Usage:**
  ```bash
  git clone <repository-url>
  ```
  Example:
  ```bash
  git clone https://github.com/username/repository.git
  ```

---

#### **3. `git status`**
- **Purpose:** Displays the state of the working directory and staging area.
- **Usage:**
  ```bash
  git status
  ```
  This shows which files are staged for commit, which are modified, and which are untracked.

---

#### **4. `git add`**
- **Purpose:** Adds files to the staging area (preparing them to be committed).
- **Usage:**
  ```bash
  git add <file-name>
  ```
  Example:
  ```bash
  git add myfile.txt
  ```
  To add all changes in the directory:
  ```bash
  git add .
  ```

---

#### **5. `git commit`**
- **Purpose:** Commits changes in the staging area to the repository with a message.
- **Usage:**
  ```bash
  git commit -m "Your commit message"
  ```
  Example:
  ```bash
  git commit -m "Added a new feature"
  ```

---

#### **6. `git push`**
- **Purpose:** Pushes the committed changes from your local repository to a remote repository (like GitHub).
- **Usage:**
  ```bash
  git push origin <branch-name>
  ```
  Example:
  ```bash
  git push origin main
  ```

---

#### **7. `git pull`**
- **Purpose:** Fetches and merges changes from a remote repository to your local repository.
- **Usage:**
  ```bash
  git pull origin <branch-name>
  ```
  Example:
  ```bash
  git pull origin main
  ```

---

#### **8. `git branch`**
- **Purpose:** List all branches or create a new branch.
- **Usage (to list branches):**
  ```bash
  git branch
  ```
- **Usage (to create a new branch):**
  ```bash
  git branch <branch-name>
  ```
  Example:
  ```bash
  git branch feature-branch
  ```

---

#### **9. `git checkout`**
- **Purpose:** Switch between branches or restore working tree files.
- **Usage (to switch branches):**
  ```bash
  git checkout <branch-name>
  ```
  Example:
  ```bash
  git checkout main
  ```

---

#### **10. `git merge`**
- **Purpose:** Merge changes from one branch into the current branch.
- **Usage:**
  ```bash
  git merge <branch-name>
  ```
  Example:
  ```bash
  git merge feature-branch
  ```

---

#### **11. `git log`**
- **Purpose:** Shows the commit history for the current branch.
- **Usage:**
  ```bash
  git log
  ```

---

#### **12. `git remote`**
- **Purpose:** Manages remote connections to a repository.
- **Usage (to view remote URLs):**
  ```bash
  git remote -v
  ```
- **Usage (to add a new remote):**
  ```bash
  git remote add origin <repository-url>
  ```
  Example:
  ```bash
  git remote add origin https://github.com/username/repository.git
  ```

---

### **Quick Summary:**
- `git init`: Initialize a Git repository.
- `git clone`: Clone a remote repository.
- `git status`: Check the status of your files.
- `git add`: Add files to staging.
- `git commit`: Commit staged changes.
- `git push`: Push changes to a remote repository.
- `git pull`: Pull changes from a remote repository.
- `git branch`: Manage branches.
- `git checkout`: Switch branches.
- `git merge`: Merge branches.
- `git log`: View commit history.
- `git remote`: Manage remote repositories.

These commands form the foundation of using Git in any workflow!