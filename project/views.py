from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project, Category, Comment, Apply, Assign, Role
from .forms import ProjectPost, ApplyPost
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth_authenticate


def list(request):
    projects = Project.objects.all().order_by('-pub_date')
    category = Category.objects.all

    return render(request, "list.html", {'projects': projects, 'category': category})


def managelist(request):
    if request.user.is_authenticated:
        user = request.user
        projects = Project.objects.filter(userid=user)
        joined_projects = Assign.objects.filter(userid=user)
        joined_list = []
        for pro in joined_projects:
            joined_list.append(pro.pid)
        return render(request, "managelist.html", {'projects': projects, 'joined_list': joined_list})

    return redirect('list')


def done(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.done == False:
        project.done = True
    else:
        project.done = False
    project.save()

    return redirect('/project/team/'+str(project_id))


def reject(request, project_id, apply_id):
    this_apply = get_object_or_404(Apply, pk=apply_id)
    this_apply.delete()

    return redirect('/project/team/'+str(project_id))


def accept(request, project_id, apply_id):
    this_apply = get_object_or_404(Apply, pk=apply_id)
    this_project = get_object_or_404(Project, pk=project_id)

    ass = Assign()
    ass.pid = this_project
    ass.userid = this_apply.userid
    ass.role = this_apply.role
    ass.save()

    this_apply.delete()
    return redirect('/project/team/'+str(project_id))


def update(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.userid = request.user
            post.pid = project_id
            post.save()

            return redirect('managelist')
    else:
        form = ProjectPost(instance=project)

        return render(request, 'update.html', {'form': form})


def team(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    apply_list = Apply.objects.filter(pid=project_id)
    assign = Assign.objects.filter(pid=project_id)
    if request.method == 'POST':
        project_detail.delete()
        return redirect('managelist')

    return render(request, 'team.html', {'project': project_detail, 'apply_list': apply_list, 'assigns': assign})


def apply(request, project_id):
    projects = get_object_or_404(Project, pk=project_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ApplyPost(request.POST)
            if form.is_valid():
                apply = form.save(commit=False)
                apply.pid = projects
                apply.userid = request.user
                apply.save()
                return redirect('/project/'+str(project_id))
        else:
            form = ApplyPost(request.POST)
            return render(request, 'apply.html', {'form': form})
    else:
        messages.success(request, '로그인이 필요합니다!')
        return redirect('list')


def cat_filter(request, cat_id):
    category = Category.objects.all
    projects = Project.objects.filter(category=cat_id)
    return render(request, "list.html", {'projects': projects, 'category': category})


def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    comment = Comment.objects.filter(pid=project_id)

    if request.user.is_authenticated:
        ass = Assign.objects.filter(pid=project_detail, userid=request.user)

    # 이미 가입했는지 확인
    try:
        if not ass:
            assign_check = False
        else:
            assign_check = True
    except:
        assign_check = True

    print(assign_check)
    project_detail.hit += 1
    project_detail.save()

    #  댓글작성
    if request.method == 'POST':
        if request.user.is_authenticated:
            cbody = request.POST['comment_body']
            newcomment = Comment()
            newcomment.pid = project_detail
            newcomment.userid = request.user
            newcomment.comment = cbody
            newcomment.save()
        else:
            print("로그인 안되있음")

    return render(request, "detail.html", {'project': project_detail, 'comment': comment, 'assign_check': assign_check})


def post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProjectPost(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.userid = request.user
                post.save()

                newassign = Assign()
                newassign.role = get_object_or_404(Role, pk=5)
                newassign.pid = get_object_or_404(Project, pk=post.pid)
                newassign.userid = request.user

                newassign.save()
                return redirect('list')
        else:
            form = ProjectPost()
            return render(request, 'post.html', {'form': form})
    else:
        messages.success(request, '로그인이 필요합니다!')
        return redirect('list')


def comdel(request, com_id):
    nowcom = get_object_or_404(Comment, pk=com_id)
    if request.user == nowcom.userid:
        nowcom.delete()
    else:
        messages.success(request, '다른 사람의 글은 지울 수 없습니다!')
    return redirect('/project/'+str(nowcom.pid))
